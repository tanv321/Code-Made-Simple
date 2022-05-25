from django.db import models

# Create your models here.
class blogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    def __str__(self):
        return f"{self.title}"
    
