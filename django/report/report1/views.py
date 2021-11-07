from django.shortcuts import render
from .models import Report
from django.http import HttpResponse

# Create your views here.

def defindex(request):
    return render(request, "report1/index.html", {
        "reports": Report.objects.all()
    })

def report(request):
    # report = Report.objects.get(id=report_id)
    # return render(request, "report1/report.html", {
    #     "report": report.id
    # })
    return HttpResponse("report")