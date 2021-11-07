from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
import datetime

# from report.firstreport.models import Report

# Create your views here.
def index_reports(request):    
    return render(request, "firstreport/index.html", {
        "a": Report.objects.all()
    })

def index(request): 
    date1 = datetime.datetime(2021, 10, 14)
    date2 = datetime.datetime(2021, 10, 15)
    a = date2 - date1 + datetime.timedelta(days=1)  
     
    return HttpResponse("Result: " + str(a.days))

def report(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, "firstreport/report.html", {
        "report": report
    })
