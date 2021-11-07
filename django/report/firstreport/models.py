from django.db import models
import datetime

# Create your models here.
class Report(models.Model):
    city = models.CharField(max_length=64)
    customername = models.CharField(max_length=64)
    startdate = models.DateField()
    finishdate = models.DateField()
    # duration = models.IntegerField(default=duration_def(self))
    @property
    def duration_def(self):
        a = self.finishdate - self.startdate + datetime.timedelta(days=1)
        return a.days

    
    
    def __str__(self):
        return f"{self.city} - {self.customername} - {self.startdate} - {self.finishdate}"