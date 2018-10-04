from django.db import models
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=30)
    
class Post(models.Model):
    contenido = models.CharField(max_length = 150)
    posted_by = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    
