from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Mantenimiento)
admin.site.register(Lavado)
admin.site.register(RecargaCombustible)
admin.site.register(Gasolinera)
admin.site.register(TipoLavado)
admin.site.register(TipoMantenimiento)
admin.site.register(TipoVehiculo)
admin.site.register(TipoCombustible)
admin.site.register(MarcaVehiculo)
admin.site.register(Local)
admin.site.register(Odometro)