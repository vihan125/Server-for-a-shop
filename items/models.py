from django.db import models

# Create your models here.

class items(models.Model):
    Key = models.IntegerField()
    name = models.CharField(max_length=250)
    price = models.FloatField()
