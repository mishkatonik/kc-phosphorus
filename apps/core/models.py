from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class PostCity(models.Model):
#     city = models.CharField(max_length=50)

class Location(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    city = models.CharField(max_length=160)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=160)
    
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)