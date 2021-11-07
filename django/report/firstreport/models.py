from django.db import models
# import datetime
from datetime import datetime

# Create your models here.


class Report(models.Model):
    city = models.CharField(max_length=64)
    customername = models.CharField(max_length=64)
    startdate = models.DateField()
    finishdate = models.DateField()
    duration = models.IntegerField()
    
    # duration = models.DurationField()
    # @property
    # def duration_def(self):
    #     a = self.finishdate - self.startdate + datetime.timedelta(days=1)
    #     return a.days

    def save(self, *args, **kwargs):
        """
        Should set duration field to total time between out and in data.
        """
        a = self.finishdate - self.startdate
        self.duration = a.days + 1
        super(Report, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.city} - {self.customername} - {self.startdate} - {self.finishdate}"
