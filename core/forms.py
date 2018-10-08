from django import forms

# create a form for our myUser model
#from .models import myUser

class ContactForm(forms.Form):
	"""docstring for RegisterForm
	"""
	SubjectHeadlineChoice = (
		('ads', 'Advertising'),
		('general', 'General'), 
		('com_abs_similar', 'Compaint/Abuse'),
		('', '')
	)

	inputName = forms.CharField(max_length = 30)
	inputText = forms.CharField(widget=forms.Textarea())
	inputEmail = forms.EmailField(widget=forms.EmailInput())
	inputSubject = forms.CharField(choices=SubjectHeadlineChoice, default = "General")