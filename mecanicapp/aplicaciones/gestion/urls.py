from django.urls import path
from .views import *
from .views_core import *
from .views_pdf import *


app_name = 'gestion'

urlpatterns = [
    
    path('dashboard/',                DashboardView.as_view(),         name = 'dashboard'),


    #********************************PATHS DE DATOS AUXILIARES***********************************

    path('list_marca/',               MarcaView.as_view(),             name = 'marcas'),

    path('list_tipovehiculo/',        TipoVehiculoView.as_view(),      name = 'tipovehiculo'), 

    path('list_tipomantenimiento/',   TipoMantenimientoView.as_view(), name = 'tipomantenimiento'),
    path('update_tipomantenimiento/<int:pk>/',   TipoMantenimientoUpdateView.as_view(), name = 'update_tipomantenimiento'),

    path('list_tipolavado/',          TipoLavadoView.as_view(),        name = 'tipolavado'),
    path('update_tipolavado/<int:pk>/',          TipoLavadoUpdateView.as_view(),        name = 'update_tipolavado'),

    path('list_tipocombustible/',     TipoCombustibleView.as_view(),   name = 'tipocombustible'),

    path('list_lavadero/',               LavaderoView.as_view(),             name = 'lavadero'),
    path('update_lavadero/<int:pk>/',    LavaderoUpdateView.as_view(),       name = 'update_lavadero'),
    
    path('list_taller/',               TallerView.as_view(),             name = 'taller'),
    path('update_taller/<int:pk>/',    TallerUpdateView.as_view(),       name = 'update_taller'),

    path('list_gasolinera/',          GasolineraView.as_view(),        name = 'gasolinera'),
    path('update_gasolinera/<int:pk>/',          GasolineraUpdateView.as_view(),        name = 'update_gasolinera'),    
    

    #********************************PATHS DE VEHÍCULO*******************************************

    path('list_vehiculo/',            VehiculoListView.as_view(),   name = 'vehiculo'),
    
    path('create_vehiculo/',          VehiculoCreateView.as_view(), name = 'create_vehiculo'),
    
    path('update_vehiculo/<int:pk>/', VehiculoUpdateView.as_view(), name = 'update_vehiculo'),


    #********************************PATHS DE MANTENIMIENTO**************************************

    path('list_mantenimiento/',            MantenimientoListView.as_view(),   name = 'mantenimiento'),

    path('create_mantenimiento/',          MantenimientoCreateView.as_view(), name = 'create_mantenimiento'),

    path('update_mantenimiento/<int:pk>/', MantenimientoUpdateView.as_view(), name = 'update_mantenimiento'),
    

    #**********************************PATHS DE LAVADO*******************************************

    path('list_lavado/',            LavadoListView.as_view(),   name = 'lavado'),

    path('create_lavado/',          LavadoCreateView.as_view(), name = 'create_lavado'),

    path('update_lavado/<int:pk>/', LavadoUpdateView.as_view(), name = 'update_lavado'),


    #**********************************PATHS DE RECARGAS******************************************

    path('list_recarga/',            RecargaCombustibleListView.as_view(),   name = 'recarga'),

    path('create_recarga/',          RecargaCombustibleCreateView.as_view(), name = 'create_recarga'),

    path('update_recarga/<int:pk>/', RecargaCombustibleUpdateView.as_view(), name = 'update_recarga'),

    
    #**************************************PATHS DE PDF********************************************
    path('lavados/pdf/<int:pk>/', AverPDF.as_view(), name = "vehiculos_pdf")
]