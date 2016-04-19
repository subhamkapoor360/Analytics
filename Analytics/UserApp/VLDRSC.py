from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
import json
from UtilsApp.utils import *
import requests
from UserApp.models import *
from validate_email import validate_email


def register_userVLDRSC(rscDict):
	rCode,rStr = '0',None
	user_id = rscDict['userId']
	if user_id in rscDict['userId_list']:
		rCode,rStr = "1","User id exists"
		return rCode,rStr,rscDict
	email_id = rscDict['emailId']
	if email_id in rscDict['email_list']:
		rCode,rStr = "2","EmailId registered already"
		return rCode,rStr,rscDict
	if validate_email(email_id,verify=True) != True:
		rCode,rStr = "3","Invalid EmailId"
		return rCode,rStr,rscDict
	return rCode,rStr,rscDict


