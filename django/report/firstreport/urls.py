from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_reports, name="reports"),
    path('timedelta', views.index),  
    # path('firstreport', views.index_reports),
    # path("<str:var>", views.testvar),
    # path("<int:report_id>", views.report, name="report"),
    # path("reports", views.report, name="report"),
    path("<int:report_id>", views.report, name="report")  
]