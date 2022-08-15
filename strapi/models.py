from django.db import models

# Create your models here.


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