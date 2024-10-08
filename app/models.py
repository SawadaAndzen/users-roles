from django.db import models

# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.ManyToManyField(Roles)
    
    def __str__(self):
        
        return self.name