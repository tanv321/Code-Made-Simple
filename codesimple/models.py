from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser #we can use AbstractUser to make our User model 
from django.contrib.auth.models import User


# Create your models here.
class blogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    created_by = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.title}"
    
