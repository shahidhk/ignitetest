from django.db import models

# Create your models here.
class Student(models.Model):
	stdChoices=(
		('', 'Select your class'),
		('six' , '6th Standard'),
		('seven' , '7th Standard'),
		('eight' , '8th Standard'),
		('nine' , '9th Standard'),
		('ten' , '10th Standard'),
	)

	name = models.CharField(max_length=60, verbose_name = 'What is your Name?')
	rollno = models.CharField(max_length=10, verbose_name = 'What is your Roll number?')
	std = models.CharField(choices=stdChoices, max_length= 50, verbose_name = 'Which Class are you in?', default=1, blank=False)
	school = models.CharField(max_length = 200, verbose_name = 'Name of your school')
	place = models.CharField(max_length = 60, verbose_name = 'Where are you from?')
	email = models.EmailField(blank=True, verbose_name = 'What is your Email?', null=True)
	phone = models.CharField(max_length=12, verbose_name = 'What is your contact number?')
	altphone = models.CharField(max_length=12, blank=True, verbose_name = 'What is your alternate contact number?', null=True)

	def __unicode__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=200, verbose_name = "Enter your School's name")
	address = models.TextField(max_length=500, verbose_name = 'What is the address?')
	email = models.EmailField(verbose_name = 'Official Email address')
	phone1 = models.CharField(max_length=12, verbose_name = 'Office phone number')
	phone2 = models.CharField(max_length=12, verbose_name = 'Other phone number')
	person = models.CharField(max_length=60, verbose_name = 'Person to contact')
	mobile = models.CharField(max_length=12, verbose_name = 'Mobile number of contact person')

	def __unicode__(self):
		return self.name