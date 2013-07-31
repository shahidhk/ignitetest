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
		if scForm.is_valid() and not stForm.is_valid():
			scForm.save()
			msg = 'You have successfully registered'
			scForm = SchoolForm()
		elif stForm.is_valid() and not scForm.is_valid():
			stForm.save()
			msg = 'You have successfully registered'
			stForm = StudentForm()
		elif stForm.is_valid() and scForm.is_valid():
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

def formview(request):

	if request.method == 'POST':
		scForm = SchoolForm(request.POST)
		if scForm.is_valid():
			scForm.save()
	else:
		scForm = SchoolForm()
	to_return={
			'scForm':scForm
		}
	
	return render(request, 'form.html', to_return)

def generate_spreadsheet(request):
	dat = Student.objects.all()
	print dat

	#ballots = dat.ballots.all()
	
	response = render_to_response("registration.html", {
		#'ballots': ballots.items(),
		#'votes': votes,
	})
	filename = "registrations%s.xls" % (dat.year_num)
	response['Content-Disposition'] = 'attachment; filename='+filename
	response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'

	return response