from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)

class Customer(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    mobile = models.CharField(validators=[mobile_regex],unique=True,max_length=250)
    age = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    health_condition = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class Trainer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    mobile = models.CharField(validators=[mobile_regex],unique=True,max_length=250)
    username = models.CharField(max_length=250,default=True)
    password = models.CharField(max_length=250)
    certification = models.CharField(max_length=250)
    stream = models.CharField(max_length=250)
    about = models.TextField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username