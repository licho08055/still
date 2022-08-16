from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    
    
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        
        
        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


    def create_user(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))
        
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))
        
        
        return self.create_user(email,password,**extra_fields)
    

class User(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=90,unique=True)

def get_default_something():
        return {'name': ['ben'], 'numberFriends': [1]}

class People(models.Model):
    friends = models.JSONField(max_length=100,default=get_default_something)
    
    
    
    

class Planet(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    code = models.CharField(max_length=20)
    picture_url = models.CharField(max_length=600)
    
    def __str__(self):
        return self.name
    
      
class Character(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    picture_url = models.CharField(max_length=600)
    planet =  models.ForeignKey(Planet, on_delete=models.CASCADE)
    people = models.ManyToManyField(People)
    
    
    def __str__(self):
        return self.name