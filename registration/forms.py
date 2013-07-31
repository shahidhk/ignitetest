from registration.models import School, Student
from django import forms

class StudentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)
			print type(field.widget)
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					field.widget = forms.TextInput(attrs={'placeholder': field.label, 'class': 'input-xlarge'})

	class Meta:
		model = Student
		widgets = {
			'std': forms.Select(attrs={'class': 'input-xlarge'}),
			
		}
	
class SchoolForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SchoolForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					field.widget = forms.TextInput(attrs={'placeholder': field.label, 'class': 'input-xlarge'})
				if type(field.widget) == forms.Textarea:
					field.widget = forms.Textarea(attrs={'placeholder': field.label,'rows':'4', 'class': 'input-xlarge'})
	class Meta:
		model = School
		