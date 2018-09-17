from django import forms

class RegisterForm(forms.Form):
	"""docstring for RegisterForm"""
	user_name = forms.CharField(max_length = 30)
	user_email = forms.EmailField()
	user_password = forms.CharField()

class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	user_username_email = forms.CharField()
	user_password = forms.CharField()
		
		