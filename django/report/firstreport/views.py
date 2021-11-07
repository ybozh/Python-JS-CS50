from django.shortcuts import render
from django.http import HttpResponse
from .models import Report

# from report.firstreport.models import Report

# Create your views here.
def index_reports(request):    
    return render(request, "firstreport/index.html", {
        "a": Report.objects.all()
    })

def index(request):    
    return HttpResponse("Hello")

def report(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, "firstreport/report.html", {
        "report": report
    })
