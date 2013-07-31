# From django
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User, Group

# From models
from registration.models import School, Student

#From Forms
from registration.forms import SchoolForm, StudentForm	

def home(request):
	msg = ''
	if request.method == 'POST':
		scForm = SchoolForm(request.POST)
		stForm = StudentForm(request.POST)
		sc = scForm.is_valid()
		st = stForm.is_valid()
		if sc and not ss:
			scForm.save()
			msg = 'You have successfully registered'
			scForm = SchoolForm()
		elif st and not sc:
			stForm.save()
			msg = 'You have successfully registered'
			stForm = StudentForm()
		elif st and sc:
			scForm.save()
			stForm.save()
			msg = 'You have successfully registered'
			scForm = SchoolForm()
			stForm = StudentForm()
	else:
		scForm = SchoolForm()
		stForm = StudentForm()
	to_return={
			'scForm':scForm,
			'stForm':stForm,
			'msg' : msg
		}
	return render(request, 'home.html', to_return)