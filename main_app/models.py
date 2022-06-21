from django.db import models

# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    visits = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
