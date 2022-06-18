from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import authUser


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class UserForm(ModelForm):
    class Meta:
        model = authUser
        fields = '__all__'
        exclude = ['user']