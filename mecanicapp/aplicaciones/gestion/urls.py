from django.urls import path
from .views import *


app_name = 'gestion'

urlpatterns = [
    
    path('dashboard/',              DashboardView.as_view(),         name = 'dashboard'),

    path('list_marca/',             MarcaView.as_view(),             name = 'marcas'),

    path('list_tipovehiculo/',      TipoVehiculoView.as_view(),      name = 'tipovehiculo'), 

    path('list_tipomantenimiento/', TipoMantenimientoView.as_view(), name = 'tipomantenimiento'),

    path('list_tipolavado/',        TipoLavadoView.as_view(),        name = 'tipolavado'),

    path('list_local/',             LocalView.as_view(),             name = 'local'),

    path('list_gasolinera/',        GasolineraView.as_view(),        name = 'gasolinera'),

    path('list_odometro/',          OdometroView.as_view(),          name = 'odometro'),

]