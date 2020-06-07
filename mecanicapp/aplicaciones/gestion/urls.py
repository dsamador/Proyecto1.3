from django.urls import path
from .views import *


app_name = 'gestion'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('list_marca/', MarcaView.as_view(), name = 'marcas'),
]