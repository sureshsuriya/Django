from django.db import models

# Create your models here.
class logdb(models.Model):
    name=models.CharField(max_length=30)
    passw=models.CharField(max_length=15)
    gend=models.CharField(max_length=15,default='Male')
    cou=models.CharField(max_length=14)
    num=models.CharField(max_length=10)
    img=models.ImageField(upload_to='images/',default=None)
    class meta:
        db_table='INF'