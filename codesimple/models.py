from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser #we can use AbstractUser to make our User model 
from django.contrib.auth.models import User


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    created_by = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    blogPost = models.ForeignKey(BlogPost, null = True, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
    post_id = models.PositiveSmallIntegerField(default=1)
   

    def __str__(self):
        return f"{self.created_by}"
