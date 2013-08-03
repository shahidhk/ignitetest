# From django
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User, Group

# From models
from registration.models import School, Student, Contact

#From Forms
from registration.forms import SchoolForm, StudentForm	

def home(request):
	msg = ''
	alert_type = ''
	scForm = SchoolForm()
	stForm = StudentForm()
	to_return={
			'scForm':scForm,
			'stForm':stForm,
			'msg' : msg
		}
	return render(request, 'home.html', to_return)
def studentsave(request):
	if request.method == 'POST':
		stForm = StudentForm(request.POST)
		scForm = SchoolForm()
		if stForm.is_valid():
			stForm.save()
			msg = 'You have successfully registered for the test, we will contact you soon with details of test'
			alert_type = 'success'
			stForm = StudentForm()
		else:
			msg='Please correct the errors in the form below'
			alert_type = 'error'
	else:
		scForm = SchoolForm()
		stForm = StudentForm()
	to_return={
			'scForm':scForm,
			'stForm':stForm,
			'msg' : msg,
			'alert_type' : alert_type
		}
	return render(request, 'home.html', to_return)

def schoolsave(request):
	if request.method == 'POST':
		scForm = SchoolForm(request.POST)
		stForm = StudentForm()
		if scForm.is_valid():
			scForm.save()
			msg = 'Your school have successfully registered for Ignite, we will contact you soon with details'
			alert_type = 'success'
			scForm = SchoolForm()
		else:
			msg='Please correct the errors in the form below'
			alert_type = 'error'
	else:
		scForm = SchoolForm()
		stForm = StudentForm()
	to_return={
			'scForm':scForm,
			'stForm':stForm,
			'msg' : msg,
			'alert_type' : alert_type
		}
	return render(request, 'home.html', to_return)
def contact(request):
	scForm = SchoolForm()
	stForm = StudentForm()
	msg=''
	alert_type=''
	if request.method == 'POST':
		data=request.POST.copy()
		p=Contact.objects.create(name=data['name'],email=data['email'],www=data['www'],body=data['body'])
		p.save()
		msg="Thank you, we will contact you soon."
		alert_type = 'success'
	to_return={
			'scForm':scForm,
			'stForm':stForm,
			'msg' : msg,
			'alert_type' : alert_type
		}
	return render(request, 'home.html', to_return)