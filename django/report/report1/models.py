from django.db import models

# Create your models here.
class Report(models.Model):
    customer = models.CharField(max_length=64)
    startdate = models.DateField()
    duration = models.IntegerField()
