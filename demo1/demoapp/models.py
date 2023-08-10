from django.db import models

# Create your models here.
class dmdb(models.Model):
    name=models.CharField(max_length=30)
    passw=models.CharField(max_length=15)
    phonenum=models.CharField(max_length=10)
    img=models.ImageField(upload_to='images/',default=None)
    class meta:
        db_table='demo'
