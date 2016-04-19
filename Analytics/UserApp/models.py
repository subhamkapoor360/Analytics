from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserAccount(models.Model):
	userId = models.CharField(max_length=255,primary_key=True)
	name  = models.CharField(max_length=255)
	gender =  models.CharField(max_length=255, null = True, blank = True)
	dateOfRegistration = models.DateTimeField(auto_now_add = True)
	mobileNo = models.CharField(max_length = 255, unique = True, db_index = True)
	emailId = models.EmailField(max_length = 255, db_index = True)

	def __unicode__(self):
		return str(self.userId)+' '+ str(self.name)+' '+str(self.mobileNo) +' '+str(self.emailId)