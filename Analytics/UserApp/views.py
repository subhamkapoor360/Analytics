from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
import json
from django.http import HttpResponse
from UserApp.GETRSC import *
from UserApp.VLDRSC import *
from UserApp.requestUtils import *
from UserApp.coreEngine import *
from UtilsApp.utils import *

# Create your views here.
@csrf_exempt
def register_user(request):
	print "register"
	response={}
	rCode, rStr, rscDict = getNCheckregister_user(request)
	if rCode == '0':
		rCode, rStr, rscDict = register_userGETRSC(rscDict)
		if rCode == '0':
			rCode, rStr, rscDict = register_userVLDRSC(rscDict)
			if rCode == '0':
				rCode, rStr, rscDict = register_userCoreEng(rscDict)
	else:
		pass
	response, responseTypeHeader = returnResponse(
													rCode, rStr, 'common', response,\
													rscDict['details'], rscDict['responseType']
												)
	return HttpResponse(response, content_type=responseTypeHeader)
	
@csrf_exempt
def reg_user_page(request):
	return render(request, "index.html")

def login_user(request):
	response={}
	rCode, rStr, rscDict = getNChecklogin_user(request)
	if rCode == '0':
		rCode, rStr, rscDict = login_userGETRSC(rscDict)
		if rCode == '0':
			rCode, rStr, rscDict = login_userVLDRSC(rscDict)
			if rCode == '0':
				rCode, rStr, rscDict = login_userCoreEng(rscDict)
	else:
		pass
	response, responseTypeHeader = returnResponse(
													rCode, rStr, 'common', response,\
													rscDict['details'], rscDict['responseType']
												)
	return HttpResponse(response, content_type=responseTypeHeader)