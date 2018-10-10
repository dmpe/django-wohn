from django import forms

# add crispy imports for sending (helper)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

class ContactForm(forms.Form):
	"""
	docstring for RegisterForm
	https://stackoverflow.com/a/31035591
	"""
	SubjectHeadlineChoice = (
		('ads', 'Advertising'),
		('general', 'General Questions'), 
		('com_abs_similar', 'Compaints/Abuse'),
		('help_me', 'Help me with something')
	)

	inputName = forms.CharField(required=True, label = "Name", 
		max_length = 30)
	# we can have more than 255 chars in the message, hence TextField
	# and not CharField
	inputText = forms.CharField(label = "Your message for us is....", widget = forms.Textarea, 
		required=True)
	inputEmail = forms.EmailField(label = "Email", required=True, 
		widget=forms.EmailInput())
	inputSubject = forms.CharField(label = "Choose the subject", required=True, 
		choices=SubjectHeadlineChoice, default = "general")

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)()
		self.helper = FormHelper()
		self.helper.form_id = "contact-form"
		self.helper.form_method = "POST"
		self.helper.form_action = reverse('submit_form')
		self.helper.add_input(Submit("subbmit", "Submit", css_class = "btn btn-primary"))















