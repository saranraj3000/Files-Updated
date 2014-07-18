from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.http import HttpResponse
from julyapp.models import *
from julyapp.forms import contactform
from julyapp.forms import districtform
from julyapp.forms import UserForm
from julyapp.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from datetime import datetime
from django import forms

# Create your views here.

#set_test_cookie()
#test_cookie_worked()
#delete_test_cookie()

def homepage (request):
    request.session.set_test_cookie()
    #username=request.session['username']
    return render(request, 'index.html', locals())

@login_required (login_url='/notlogin')
def mainpage (request):
    #username=request.session['username']
    #response = HttpResponse()
    #response = render(request, template)
    # if request.session.test_cookie_worked():
    #     print "Your Cookie is Worked"
    #     #response.set_cookie('id', 'saran')
    #     #id = request.COOKIES.get('id')
    #     return render(request, 'cookie.html', locals())
    #     if request.set_cookie('sarancookie'):
    #         request.session.delete_test_cookie()
    return render(request, 'mainpage.html', locals())


@login_required (login_url='/notlogin')
def sarancookie (request):
    username=request.session['username']
    # import ipdb
    # ipdb.set_trace()
    response = render_to_response('cookie.html')
    response.set_cookie('id', 1)
    id = request.COOKIES.get('id')
    return render(request, 'cookie.html', locals())
        

@login_required (login_url='/notlogin')
def hello (request):
    username=request.session['username']
    return HttpResponse ("Hello World")

@login_required (login_url='/notlogin')
def hello1 (request):
    #username=request.session['username']
    return HttpResponse ("Hi Saran")

def add (request):
    a=5
    b=10
    c=a+b
    return render(request, 'add.html', locals())

@login_required (login_url='/notlogin')
def name (request):
	username=request.session['username']
	form1=contactform()
	if request.POST: 
		#import ipdb;ipdb.set_trace()
		first_name=request.POST['firstname']
		last_name=request.POST['lastname']
		sex=request.POST['sex']
		uploadfile=request.FILES['uploadfile']
		age=request.POST['age']
		dob=request.POST['dob']
		email1=request.POST['email']
		try:
			marriage=request.POST['marriage']
		except Exception:
			marriage=False
		data=Contact(first_name=first_name,last_name=last_name,sex=sex,uploadfile=uploadfile,age=age,dob=dob,email1=email1,marriage=marriage,)
		data.save()
	username=request.session['username']
	b=Contact.objects.all()
	#name=str(firstname)+str(lastname)
	return render(request, 'name.html', locals())

@login_required (login_url='/notlogin')
def namemodel (request):
	username=request.session['username']
	form1=contactform()
	if request.POST: 
		#import ipdb;ipdb.set_trace()
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		sex=request.POST['sex']
		uploadfile=request.FILES['uploadfile']
		age=request.POST['age']
		dob=request.POST['dob']
		email1=request.POST['email1']
		try:
			marriage=request.POST['marriage']
		except Exception:
			marriage=False
		data=Contact(first_name=first_name,last_name=last_name,sex=sex,uploadfile=uploadfile,age=age,dob=dob,email1=email1,marriage=marriage,)
		data.save()
	b=Contact.objects.all()
	    #name=str(firstname)+str(lastname)
	return render(request, 'namemodel.html', locals())

@login_required (login_url='/notlogin')
def edit (request,id):
	username=request.session['username']
	b=Contact.objects.get(id=id)
	if request.POST:
		b.first_name=request.POST['firstname']
		b.last_name=request.POST['lastname']
		b.sex=request.POST['sex']
		b.uploadfile=request.FILES['uploadfile']
		b.age=request.POST['age']
		b.dob=request.POST['dob']
		b.email1=request.POST['email']
		b.marriage=request.POST['marriage']
		b.save()
		return HttpResponseRedirect('/list')
	return render(request, 'edit.html', locals())

def list (request):
	username=request.session['username']
	b=Contact.objects.all()
	return render(request, 'list.html', locals())

@login_required (login_url='/notlogin')
def delete (request,id):
	username=request.session['username']
	b=Contact.objects.get(id=id)
	if request.POST:
		b.delete()
		return HttpResponseRedirect('/list')
	return render(request, 'delete.html', locals())
		
	#return render(request, 'edit.html', locals())
	#return HttpResponseRedirect('/list')

@login_required (login_url='/notlogin')
def dontdelete (request):
	username=request.session['username']
	return HttpResponseRedirect('/list')
	#return render(request, 'list.html', locals())	

@login_required (login_url='/notlogin')
def district (request):
	username=request.session['username']
	form2=districtform()
	if request.POST: 
		#import ipdb;ipdb.set_trace()
		district_name=request.POST['district_name']
		data=District(district_name=district_name,)
		data.save()
	b=District.objects.all()
	return render(request, 'district.html', locals())

def districtlist (request):
	username=request.session['username']
	b=District.objects.all()
	return render(request, 'districtlist.html', locals())

def usersignup (request):
	# import ipdb
	# ipdb.set_trace()
	if request.method=='POST': 
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			user_form = UserForm
			profile_form = UserProfileForm
		return HttpResponseRedirect('.')
	else:
		user_form = UserForm
		profile_form = UserProfileForm
	return render(request, 'usersignup.html', locals())

def userlogin (request):
	if request.method=='POST':
		#import ipdb
		#ipdb.set_trace()
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				request.session['username']=username
				#print request.session['session']
				if request.session['username']==username:
					print 'Login in '+username
					return HttpResponseRedirect('mainpage')
				# else:
				# 	return render(request, 'notlogin.html', locals())
				else:
					return HttpResponse("Your Login Account is Disabled")
			else:
				return render(request, 'userlogin.html', locals())			
		else:
			return render(request, 'notlogin.html', locals())
	else:
			return render(request, '.', locals())

def userlogout (request):
	logout(request)
	return HttpResponseRedirect('.')

def logincheck (request):
	#username=request.session['username']
	return HttpResponse('Since You are Logged in, You can see this text')

def notlogin (request):
	return render (request, 'notlogin.html')

def index123(request):
        username=request.session['username']
        # import ipdb
        # ipdb.set_trace()
        visits = int( request.COOKIES.get('visits', '0') )

        response =  HttpResponse('cookie.html')

        if request.COOKIES.has_key('last_visit' ):
                last_visit = request.COOKIES['last_visit']
                # the cookie is a string - convert back to a datetime type
                last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
                curr_time = datetime.now()
                if (curr_time-last_visit_time).days > 0:
                        # if at least one day has gone by then inc the visit count.
                        response.set_cookie('visits', visits + 1 )
                        response.set_cookie('last_visit', datetime.now())
        else:
                response.set_cookie('last_visit', datetime.now())

        return response

# def saransession (request):
# 	request.session['username']=request.POST["userlogin.username"]
# 	#print request.session['session']
# 	if request.session['username']==request.POST["userlogin.username"]:
# 		print 'Loged in "emisf13"'
# 	return HttpResponseRedirect('.')

# def session(request):
#     if request.method == 'POST':
#         if request.session.test_cookie_worked():
#             request.session.delete_test_cookie()
#             return HttpResponse("You're logged in.")
#         else:
#             return HttpResponse("Please enable cookies and try again.")
#     request.session.set_test_cookie()
#     return render_to_response('index.html')

# def nameform (request):
# 	username=request.session['username']
# 	nameform=NameForm()
# 	if request.POST: 
# 		#import ipdb;ipdb.set_trace()
# 		your_name=request.POST['yourfirst_name']
# 		last_name=request.POST['last_name']
# 		sex=request.POST['sex']
# 		uploadfile=request.FILES['uploadfile']
# 		age=request.POST['age']
# 		dob=request.POST['dob']
# 		email1=request.POST['email1']
# 		try:
# 			marriage=request.POST['marriage']
# 		except Exception:
# 			marriage=False
# 		data=Contact(first_name=first_name,last_name=last_name,sex=sex,uploadfile=uploadfile,age=age,dob=dob,email1=email1,marriage=marriage,)
# 		data.save()
# 	b=Contact.objects.all()
# 	    #name=str(firstname)+str(lastname)
# 	return render(request, 'namemodel.html', locals())
# --------------
def get_name(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})