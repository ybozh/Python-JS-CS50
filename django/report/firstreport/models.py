from django.db import models

# Create your models here.
class Report(models.Model):
    city = models.CharField(max_length=64)
    customername = models.CharField(max_length=64)
    startdate = models.DateField()
    finishdate = models.DateField()

    def __str__(self):
        return f"{self.city} - {self.customername} - {self.startdate} - {self.finishdate}"