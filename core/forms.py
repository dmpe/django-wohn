from django import forms
from django.urls import reverse

# add crispy imports for sending (helper)
from crispy_forms.helper import *
from crispy_forms.layout import *

class ContactForm(forms.Form):
	"""
	Keep this as cripsy form !
	"""
	SubjectHeadlineChoice = (
		('general', 'General Questions'), 
		('ads', 'Advertising'),
		('com_abs_similar', 'Compaints/Abuse'),
		('help_me', 'Help me with something')
	)

	inputName = forms.CharField(required=True, label = "Name", 
		max_length = 30)
	inputEmail = forms.EmailField(label = "Email", required=True, 
		widget=forms.EmailInput())
	inputSubject = forms.ChoiceField(label = "Message deals with...", required=True, 
		choices=SubjectHeadlineChoice)
	# we can have more than 255 chars in the message, hence TextField
	# and not CharField
	inputText = forms.CharField(label = "Your message is about....", widget = forms.Textarea, 
		required=True)














