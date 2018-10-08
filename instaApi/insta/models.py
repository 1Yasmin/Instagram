from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
# Tabla de Post de los usuarios
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 250)
    posted_by = models.ForeignKey(User, related_name = u'creador', null=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name = u'gente')

