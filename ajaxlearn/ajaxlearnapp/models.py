from django.db import models

# Create your models here.
class mypost(models.Model):
    name=models.CharField(max_length=100)
    password=models.TextField()
