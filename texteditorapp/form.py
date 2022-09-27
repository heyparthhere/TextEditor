from django import forms
from .models import ContactUs
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.db import models
from django.forms import fields, widgets
from django.forms.forms import Form

class UserRegistration(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta():
        model = User
        fields = ["first_name","last_name","email","password1","password2"]

        widgets = {

            
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name...'}),
            'last_name' :  forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Lat Name...'}),
            'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email ID...'}),
        }


class UserLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password...'}))
    class Meta():
        model = User
        ['username','password']

    
class Contactform(forms.ModelForm):
    class Meta():
        model = ContactUs
        fields = ["msg", "Email", "name"][::-1]
        widgets = {

            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name...'}),
            'Email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email...'}),
            'msg' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Response...'})
        }
