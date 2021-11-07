from django.urls import path
from . import views

# app_name = "report1"
urlpatterns = [
    path('', views.defindex, name="index"),
    # path("<str:var>", views.testvar),
    # path("<int:report_id>", views.report, name="report"),
    path("reports", views.report, name="report")  
]