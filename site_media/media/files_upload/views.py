from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from julyapp.models import *
# Create your views here.
def homepage (request):
    return render(request, 'index.html', locals())
def mainpage (request):
    return render(request, 'mainpage.html', locals())
def hello (request):
    return HttpResponse ("Hello World")
def hello1 (request):
    return HttpResponse ("Hi Saran")
def add (request):
    a=5
    b=10
    c=a+b
    return render(request, 'add.html', locals())
def name (request):
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
	b=Contact.objects.all()
	    #name=str(firstname)+str(lastname)
	return render(request, 'name.html', locals())

def edit (request,id):
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
	b=Contact.objects.all()
	return render(request, 'list.html', locals())

def delete (request,id):
	b=Contact.objects.get(id=id)
	if request.POST:
		b.delete()
		return HttpResponseRedirect('/list')
	return render(request, 'delete.html', locals())
		
	#return render(request, 'edit.html', locals())
	#return HttpResponseRedirect('/list')
def dontdelete (request):
	return HttpResponseRedirect('/list')
	#return render(request, 'list.html', locals())	