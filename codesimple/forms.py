from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import blogPost
from django import forms
from django.forms import ModelForm, Textarea
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class blogPostForm(ModelForm):
    class Meta:
        model = blogPost
        exclude = ('created_by',)
        fields = [
            'title',
            'body',
        ]
        widgets = {
            'body': Textarea()
        }
