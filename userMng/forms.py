from django import forms

# create a form for our myUser model
#from .models import myUser

class RegisterForm(forms.Form):
	"""docstring for RegisterForm
	"""
	inputUsername = forms.CharField(max_length = 30)
	inputEmail = forms.EmailField(widget=forms.EmailInput())
	inputNewPassword = forms.CharField(widget=forms.PasswordInput())
	inputConfirmNewPassword = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
	"""docstring for LoginForm
	Users can login either via username or email. 
	Hence, input type="text"
	"""
	user_username_email = forms.CharField(widget=forms.TextInput())
	user_password = forms.CharField(widget=forms.PasswordInput())
		
		