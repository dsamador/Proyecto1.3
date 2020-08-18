from django.urls import path
from .views import ReportMantenimiento,ReportLavado,ReportRecarga


urlpatterns = [
    path('mantenimientos/', ReportMantenimiento.as_view(), name='reporte_mantenimientos'),
    path('lavados/', ReportLavado.as_view(), name='reporte_lavados'),
    path('recargas/', ReportRecarga.as_view(), name='reporte_recargas'),
]