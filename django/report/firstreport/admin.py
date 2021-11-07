from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('city', 'customername', 'startdate', 'finishdate')

# Register your models here.
admin.site.register(Report)
