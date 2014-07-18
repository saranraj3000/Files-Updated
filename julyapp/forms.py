from django import forms
from julyapp.models import Contact
from julyapp.models import District
from julyapp.models import User
from julyapp.models import UserProfile
from julyapp.models import get_name

class contactform(forms.ModelForm):
	class Meta:
		model=Contact
#	first_name=forms.CharField(required=True)
#	last_name=forms.CharField(required=False)

class districtform(forms.ModelForm):
	class Meta:
		model=District

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('company', 'website')

class NameForm(forms.ModelForm):
    class Meta:
        your_name = forms.CharField(label='Your name', max_length=100)