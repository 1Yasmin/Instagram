from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Post(models.Model):
    contenido = models.CharField(max_length = 150)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
