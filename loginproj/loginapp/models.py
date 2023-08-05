from django.db import models
# Create your models here.
class StdDb(models.Model):
    sname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    class Meta:
        db_table = 'StdDB'
