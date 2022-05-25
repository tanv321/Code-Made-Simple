from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import blogPost
from django import forms
from django.forms import ModelForm
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class blogPostForm(ModelForm):
    class Meta:
        model = blogPost
        fields = '__all__'
