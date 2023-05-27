from django.db import models

# Create your models here.

""" class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    fundation=models.DateField() """

class licenciameinto(models.Model):
   id_licencia=models.AutoField(primary_key=True)
   licencia=models.CharField(max_length=20)
   estado=models.BooleanField()
   fecha_emision=models.DateField()
   fecha_vencimiento=models.DateField()

   class Meta:
        managed = False
        db_table = 'licenciameinto'