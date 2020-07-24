from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MarcaResource(resources.ModelResource):
    class Meta:
        model = MarcaVehiculo


class MarcaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    resource_class = MarcaResource


admin.site.register(Vehiculo)
admin.site.register(Mantenimiento)
admin.site.register(Lavado)
admin.site.register(RecargaCombustible)
admin.site.register(Gasolinera)
admin.site.register(TipoLavado)
admin.site.register(TipoMantenimiento)
admin.site.register(TipoVehiculo)
admin.site.register(TipoCombustible)
admin.site.register(MarcaVehiculo, MarcaAdmin)
admin.site.register(Lavadero)
admin.site.register(Taller)
