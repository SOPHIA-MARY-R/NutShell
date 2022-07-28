from operator import mod
from django.db import models

# Create your models here.
class URL(models.Model):
    uuid=models.CharField(max_length=10) #to uniquely identify a URL
    link=models.CharField(max_length=10000) # the link which is entered
    
