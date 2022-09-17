from pyexpat import model
from tabnanny import verbose
from tkinter.tix import Form
from turtle import title
from typing_extensions import ParamSpecArgs
from xml.etree.ElementTree import Comment
from attr import fields
from certifi import contents
from click import confirm
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput

from custom_user.models import MyUser
from .models import AddWork,Comment

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label='username')
    password = forms.CharField(max_length=20,widget=PasswordInput,label='password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(
        max_length=20, label='Password', widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label='Confirm', widget=forms.PasswordInput)
    def clean(self):
     
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        

        if password and confirm and password != confirm:
            raise ValidationError('Password in False!')

        values = {
            'username':username,
            'password':password
        }

        return values

class Work(forms.ModelForm):
    class Meta:
        model = AddWork
        fields = ['title', 'content', 'image', 'category', 'client']

class EditForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields = ['username', 'profile_photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['comment_author','comment_content']