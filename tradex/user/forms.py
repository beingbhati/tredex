from django.forms import fields
from user.models import MyUser
from django import forms
# from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        