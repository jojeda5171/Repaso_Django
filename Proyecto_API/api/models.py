from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    fundation=models.DateField()