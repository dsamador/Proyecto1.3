from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count
from django.forms import model_to_dict
import json
from .models import *
from .forms import *
from datetime import datetime
from django.http import JsonResponse


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_reporte_lavados(self):
        data = []
        try:
            year = datetime.now().year
            for i in range(1,13):
                total = Lavado.objects.filter(fecha__year = year, fecha__month = i).aggregate(r=Coalesce(Sum('valor'), 0)).get('r')               
                data.append(float(total))
        except:
            pass
        return data
    
    def get_reporte_mantenimientos(self):
        data = []
        try:
            year = datetime.now().year
            for i in range(1,13):
                total = Mantenimiento.objects.filter(fecha__year = year, fecha__month = i).aggregate(r=Coalesce(Sum('valor'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_reporte_recargas(self):
        data = []
        try:
            year = datetime.now().year
            for i in range(1,13):
                total = RecargaCombustible.objects.filter(fecha__year = year, fecha__month = i).aggregate(r=Coalesce(Sum('costo_total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data
    
    def get_gastos_mes_actual_mant(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for i in Vehiculo.objects.all():
                total = Mantenimiento.objects.filter(fecha__year = year, fecha__month = month, vehiculo_id=i.id).aggregate(
                    r=Coalesce(Sum('valor'), 0)).get('r')
                if total >0:
                    data.append({
                        'name': i.nombre,
                        'y':float(total)
                    })
        except expression as identifier:
            pass
        return data

    def get_gastos_mes_actual_reca(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for i in Vehiculo.objects.all():
                total = RecargaCombustible.objects.filter(fecha__year = year, fecha__month = month, vehiculo_id=i.id).aggregate(
                    r=Coalesce(Sum('costo_total'), 0)).get('r')
                if total >0:
                    data.append({
                        'name': i.nombre,
                        'y':float(total)
                    })
        except expression as identifier:
            pass
        return data

    def get_gastos_mes_actual_lava(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for i in Vehiculo.objects.all():
                total = Lavado.objects.filter(fecha__year = year, fecha__month = month, vehiculo_id=i.id).aggregate(
                    r=Coalesce(Sum('valor'), 0)).get('r')
                if total >0:
                    data.append({
                        'name': i.nombre,
                        'y':float(total)
                    })
        except expression as identifier:
            pass
        return data

    def post(self, request, *args, **kwargs):   
        data = {}          
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':

                total_lavados = Lavado.objects.all().aggregate(Sum('valor')) 
                flotante1 = float(total_lavados.get('valor__sum'))               
                lavados = json.dumps(flotante1)

                total_mantenimientos = Mantenimiento.objects.all().aggregate(Sum('valor')) 
                flotante2 = float(total_mantenimientos.get('valor__sum'))               
                mantenimientos = json.dumps(flotante2)

                total_recargas = RecargaCombustible.objects.all().aggregate(Sum('costo_total')) 
                flotante3 = float(total_recargas.get('costo_total__sum'))                          
                recargas = json.dumps(flotante3)
                
                total_todo = flotante1+flotante2+flotante3                

                datos = {
                    'lavados':[{'numero':lavados}],
                    'mantenimientos':[{'numero':mantenimientos}],
                    'recargas':[{'numero':recargas}],
                    'total_todo':[{'numero':total_todo}],                    
                }           
                return JsonResponse(datos, safe = False)

            elif action == 'carga': 
                total_gasolineras = RecargaCombustible.objects.values('gasolinera').distinct().count() 
                total_vehiculos = Vehiculo.objects.all().count()
                km = Odometro.objects.all().aggregate(Sum('distancia')) 
                total_combustible = RecargaCombustible.objects.all().aggregate(Sum('cantidad'))
                datos = {                    
                    'gas':[{'numero':total_gasolineras}],
                    'vehiculos':[{'numero':total_vehiculos}],
                    'km':[km],
                    'total_combustible':[total_combustible],
                }           
                return JsonResponse(datos, safe = False) 
            
            elif action ==  'get_gastos_mes_actual_mant':
                data = {
                    'name':'Porcentaje',
                    'colorByPoint':True,
                    'data':self.get_gastos_mes_actual_mant(),
                }
                return JsonResponse(data, safe = False)
                
            elif action ==  'get_gastos_mes_actual_reca':
                data = {
                    'name':'Porcentaje',
                    'colorByPoint':True,
                    'data':self.get_gastos_mes_actual_reca(),
                }
                return JsonResponse(data, safe = False)  

            elif action ==  'get_gastos_mes_actual_lava':
                data = {
                    'name':'Porcentaje',
                    'colorByPoint':True,
                    'data':self.get_gastos_mes_actual_lava(),
                }
                return JsonResponse(data, safe = False)  

        except Exception as e:
            data['error'] = str(e)
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador' 
        context['entity'] = 'Dashboard'
        context['reporte_lavados'] = self.get_reporte_lavados()
        context['reporte_mantenimientos'] = self.get_reporte_mantenimientos()
        context['reporte_recargas'] = self.get_reporte_recargas()   
        context['form']  = SelectForm()
        context['title'] = 'Dashboard'
        return context




"""
    Vistas de las marcas de vehiculos
"""

class MarcaView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/marca/list_marca.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in MarcaVehiculo.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = MarcaVehiculo()
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'edit':
                m = MarcaVehiculo.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'delete':
                m = MarcaVehiculo.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de marcas'                
        context['entity'] = 'Marcas'
        context['form'] = MarcaVehiculoForm()
        return context 

"""
    Vistas de los tipos de vehiculos
"""

class TipoVehiculoView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/tipovehiculo/list_tipovehiculo.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in TipoVehiculo.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = TipoVehiculo()
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'edit':
                m = TipoVehiculo.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'delete':
                m = TipoVehiculo.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos de vehiculos'                
        context['entity'] = 'Tipos de Vehiculos'
        context['form'] = TipoVehiculoForm()
        return context 

"""
    Vistas de tipos de lavados
"""

class TipoLavadoView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/tipolavado/list_tipolavado.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in TipoLavado.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = TipoLavado()
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'edit':
                m = TipoLavado.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'delete':
                m = TipoLavado.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos de lavados'                
        context['entity'] = 'Tipos de Lavados'
        context['form'] = TipoLavadoForm()
        return context
        
"""
    Vistas de Tipos de Mantenimientos
"""

class TipoMantenimientoView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/tipomantenimiento/list_tipomantenimiento.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in TipoMantenimiento.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = TipoMantenimiento()
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'edit':
                m = TipoMantenimiento.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'delete':
                m = TipoMantenimiento.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos de mantenimientos'                
        context['entity'] = 'Tipos de Mantenimientos'
        context['form'] = TipoMantenimientoForm()
        return context 
"""
    Vistas de las Gasolineras
"""

class GasolineraView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/gasolinera/list_gasolinera.html'    
    
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)Otra forma de meter seguridad
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in Gasolinera.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = Gasolinera()
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.direccion = request.POST['direccion']
                m.save()
            elif action == 'edit':
                m = Gasolinera.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.descripcion = request.POST['descripcion']
                m.direccion = request.POST['direccion']
                m.save()
            elif action == 'delete':
                m = Gasolinera.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de gasolineras'                
        context['entity'] = 'Gasolinera'
        context['form'] = GasolineraForm()
        return context 

"""
    Vistas de los locales
"""

class LocalView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/local/list_local.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in Local.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = Local()
                m.nombre = request.POST['nombre']
                m.direccion = request.POST['direccion']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'edit':
                m = Local.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.direccion = request.POST['direccion']
                m.descripcion = request.POST['descripcion']
                m.save()
            elif action == 'delete':
                m = Local.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de locales'                
        context['entity'] = 'Local'
        context['form'] = LocalForm()
        return context 
"""
    Vistas de los odometros
"""

class OdometroView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/odometro/list_odometro.html'    
    form_class = OdometroForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in Odometro.objects.all():
                    data.append(i.toJSON())
            
            elif action == 'add': #esto va de acuerdo con un input hidden en el html
                form = self.get_form() #obtiene el formulario con los datos que contiene
                if form.is_valid(): 
                    form.save()
                return JsonResponse(data)                                

            elif action == 'edit':
                m = Odometro.objects.get(pk=request.POST['id'])
                m.distancia = request.POST['distancia']
                m.vehiculo = request.POST['vehiculo']
                m.fecha = request.POST['fecha']
                m.save()
            elif action == 'delete':
                m = Odometro.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de odómetros'                
        context['entity'] = 'Odometro'
        context['form'] = OdometroForm()
        return context 


class TipoCombustibleView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/tipocombustible/list_tipocombustible.html'    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in TipoCombustible.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = TipoCombustible()
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'edit':
                m = TipoCombustible.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'delete':
                m = TipoCombustible.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos de combustibles'                
        context['entity'] = 'Tipos de combustibles'
        context['form'] = TipoCombustibleForm()
        return context 



