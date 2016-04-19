from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
import json
from UtilsApp.utils import *
import requests
from UserApp.models import *
from django.contrib.auth.models import User

def register_userGETRSC(rscDict):
	rCode,rStr = '0',None
	try:
		rscDict['userId_list'] = User.objects.all().values_list('username',flat=True)
		rscDict['email_list'] = User.objects.all().values_list('email',flat=True)
	except Exception,e:
		print str(e)
	return rCode,rStr,rscDict

def login_userGETRSC(rscDict):
	rCode,rStr = '0',None
	try:
		rscDict['user'] = User.objects.get(username=rscDict['username'])
		rscDict['site_user'] =UserAccount.objects.get(userId=rscDict['username'])
	except Exception,e:
		rCode,rStr ="1","Username doesn't exist"
		return rCode,rStr,rscDict
	return rCode,rStr,rscDict