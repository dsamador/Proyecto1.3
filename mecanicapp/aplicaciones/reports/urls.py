from django.urls import path
from .views import Report

urlpatterns = [
    path('mantenimientos/', Report.as_view(), name='reporte_mantenimientos'),
]