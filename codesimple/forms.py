from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import BlogPost, Comment
from django import forms
from django.forms import ModelForm, Textarea
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'content': Textarea()
        }


class commentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_by',)
        fields = [
            'content',
        ]
        widgets = {
            'content': Textarea()
        }
