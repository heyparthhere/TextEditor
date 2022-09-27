from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.contrib.auth.models import User

# Create your models here.

class ContactUs(models.Model):
    login_id = models.ForeignKey(User, on_delete=CASCADE)
    name=models.TextField()
    Email=models.EmailField()
    msg=models.CharField(max_length=200)