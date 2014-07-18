from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	first_name=models.CharField(
		max_length=255,
		)
	last_name=models.CharField(
		max_length=255,
		)
	sex=models.CharField(
		max_length=6,)
	uploadfile=models.FileField(
		upload_to='files_upload',
		)
	age=models.IntegerField(
		max_length=2
		)
	dob=models.DateField()
	email1=models.EmailField()
	marriage=models.BooleanField()

	def __unicode__(self):
		return ' '.join([
		self.first_name,
		self.last_name,
	# 	self.email1,
	#	self.sex,
	#	self.uploadfile,
	# 	self.age,
	# 	self.dob,
	# 	self.marriage,
	 	])
# Create your models here.
class District (models.Model):
	district_name=models.CharField(
		max_length=255,
		)

	def __unicode__(self):
		return self.district_name

class UserProfile (models.Model):
	user=models.OneToOneField(User)
	company=models.CharField(max_length=255,)
	website=models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username

class get_name (models.Model):
	your_name=models.CharField(
		max_length=255,
		)

	def __unicode__(self):
		return self.your_name