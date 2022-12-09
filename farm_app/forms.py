from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput, ModelForm
from django import forms

from .models import *

class RegistrationForm(UserCreationForm):
    # as_farmer = forms.BooleanField(label = "Register as farmer")
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'is_farmer')
        labels = {
            "is_farmer": "Register as farmer"
        }

# class FarmerRegistrationForm(RegistrationForm):
#     pass


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 128, widget = PasswordInput)

class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
        labels = {
            "name": "Farm Name"
        }