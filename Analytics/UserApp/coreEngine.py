from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
import json
from datetime import *
from UserApp.models import UserAccount
from django.contrib.auth.models import User
from django.shortcuts import redirect
from UtilsApp.utils import authenticatev1


def register_userCoreEng(rscDict):
	try:
		user = User.objects.create_user(username=rscDict['userId'],email=rscDict['emailId'],\
			password=rscDict['password'])
		x_user = UserAccount.objects.create(userId=rscDict['emailId'],name=rscDict['name']\
			,gender=rscDict['gender'],mobileNo=rscDict['mobileNo'],emailId=rscDict['emailId'])
	except Exception,e:
		print str(e)
	rCode,rStr = '0',None
	res_dict = {}
	res_dict['name']= rscDict['name']
	res_dict['emailId']= rscDict['emailId']
	res_dict['mobileNo']= rscDict['mobileNo']
	res_dict['gender']= rscDict['gender']
	res_dict['userId']= rscDict['userId']
	res_dict['password']= rscDict['password']
	rscDict['details']['register'] = res_dict
	print rscDict['details']['register']
	return rCode,rStr,rscDict

def login_userCoreEng(rscDict):
	user = rscDict['user']
	userId = rscDict['username']
	password = rscDict['password']
	site_user = rscDict['site_user']
	user_name,user = authenticatev1(userId,password)
	if user is not None:
		# the password verified for the user
		if user.is_active:
			print("User is valid, active and authenticated")
			rCode,rStr = '0','Logged In'
			rscDict['details']['user'] = user
			rscDict['details']['cuser'] =site_user
			#return redirect('home_view', pk=site_user.id)
		else:
			print("The password is valid, but the account has been disabled!")
			rCode,rStr = '1','The password is valid, but the account has been disabled!'
			#return redirect('disabled_view')
	else:
		# the authentication system was unable to verify the username and password
		print("The username and password were incorrect.")
		rCode,rStr = '2','The username and password were incorrect.'
	return rCode,rStr,rscDict