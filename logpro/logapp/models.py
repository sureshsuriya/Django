from django.db import models

# Create your models here.
class newdb(models.Model):
    r=models.CharField(max_length=30)
    b=models.CharField(max_length=15)
    g=models.CharField(max_length=15,default='Male')
    cou=models.CharField(max_length=14)
    num=models.CharField(max_length=10)
    class meta:
        db_table='newdb'