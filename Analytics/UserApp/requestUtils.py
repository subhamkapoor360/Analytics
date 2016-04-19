from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
import json
from UtilsApp.utils import *
import requests
from UserApp.models import *

def getNCheckregister_user(request):
	rCode, rStr = '0', None
	#Dictionary contains all the possible parameters those are expected in this api call
	rscDict = { 
				'name':None,
				'userId':None,
				'password':None,
				'gender':None,
				'mobileNo':None,
				'emailId':None,
				'responseType':'json',
				'details':{},
			}
	#List contains the mandatory parameters
	reqdParams = ['name','userId','mobileNo','emailId','password']
	for k,v in rscDict.items():
		if k in request.POST:
			rscDict[k]  = request.POST[k]
			if k in reqdParams:
				#Removes the received parameters
				reqdParams.remove(k)
	if len(reqdParams) != 0:
		#returns the array of not received parameters which will be sent back to client.
		rscDict['details']['paramsNotSent'] = ",".join(reqdParams)
		rCode, rStr =  RESPONSE_CODE_POSTPARAMS_ERROR, RESPONSE_STRING_POST_PARAMS
	return rCode, rStr, rscDict

def getNChecklogin_user(request):
	rCode, rStr = '0', None
	#Dictionary contains all the possible parameters those are expected in this api call
	rscDict = { 
				'username':None,
				'password':None,
				'responseType':'json',
				'details':{},
			}
	#List contains the mandatory parameters
	reqdParams = ['username','password']
	for k,v in rscDict.items():
		if k in request.POST:
			rscDict[k]  = request.POST[k]
			if k in reqdParams:
				#Removes the received parameters
				reqdParams.remove(k)
	if len(reqdParams) != 0:
		#returns the array of not received parameters which will be sent back to client.
		rscDict['details']['paramsNotSent'] = ",".join(reqdParams)
		rCode, rStr =  RESPONSE_CODE_POSTPARAMS_ERROR, RESPONSE_STRING_POST_PARAMS
	return rCode, rStr, rscDict
