from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from .models import Vehiculo, Mantenimiento, Lavado, RecargaCombustible
from .forms import VehiculoForm, MantenimientoForm, LavadoForm, RecargaCombustibleForm

from django.http import JsonResponse


class VehiculoListView(LoginRequiredMixin, ListView): #Este código funciona
    model = Vehiculo
    template_name = 'vehiculo/list_vehiculo.html'

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                #filter(usuario=self.request.user)
                for i in Vehiculo.objects.filter(usuario=self.request.user):
                    data.append(i.toJSON())     
            elif action == 'retrieveVhcl':
                data = []                
                for i in Vehiculo.objects.filter(id=request.POST['id']):                    
                    data.append(i.toJSON())                    
            elif action == 'delete':
                m = Vehiculo.objects.get(pk=request.POST['id'])
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de vehículos'    
        context['create_url'] = reverse_lazy('gestion:create_vehiculo')
        context['entity'] = 'Vehiculo'
        context['form'] = VehiculoForm
        context['desc'] = 'Vehículos'
        return context


class VehiculoCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm    
    template_name = 'vehiculo/create_vehiculo.html'
    success_url = reverse_lazy('gestion:vehiculo')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):        
        return super().dispatch(request, *args, **kwargs)    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add': #esto va de acuerdo con un input hidden en el html
                form = self.get_form() #obtiene el formulario con los datos que contiene
                if form.is_valid(): 
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de vehiculo'        
        context['list_url'] = self.success_url       
        context['action'] = 'add'        
        context['entity'] = 'Crear Vehiculo'
        context['desc'] = 'Vehículos'
        return context         

class VehiculoUpdateView(LoginRequiredMixin, UpdateView):# Este no tiene ajax
    model = Vehiculo
    form_class = VehiculoForm    
    template_name = 'vehiculo/update.html'
    success_url = reverse_lazy('gestion:vehiculo')          
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de vehiculo'        
        context['list_url'] = self.success_url       
        context['action'] = 'edit'        
        context['entity'] = 'Editar Vehiculo'
        context['desc'] = 'Vehículos'
        return context    

"""
VIEWS DE MANTENIMIENTO

"""

class MantenimientoListView(LoginRequiredMixin, ListView): #Este código funciona
    model = Mantenimiento
    template_name = 'mantenimiento/list_mantenimiento.html'

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Mantenimiento.objects.all():
                    data.append(i.toJSON())     
            elif action == 'retrieveMantenimiento':
                data = []                
                for i in Mantenimiento.objects.filter(id=request.POST['id']):                    
                    data.append(i.toJSON())                    
            elif action == 'delete':
                m = Mantenimiento.objects.get(pk=request.POST['id'])
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de mantenimientos'    
        context['create_url'] = reverse_lazy('gestion:create_mantenimiento')
        context['entity'] = 'Mantenimiento'
        context['form'] = MantenimientoForm
        context['desc'] = 'Mantenimientos y Reparaciones'
        return context

class MantenimientoCreateView(LoginRequiredMixin, CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm    
    template_name = 'mantenimiento/create_mantenimiento.html'
    success_url = reverse_lazy('gestion:mantenimiento')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):        
        return super().dispatch(request, *args, **kwargs)    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add': #esto va de acuerdo con un input hidden en el html
                form = self.get_form() #obtiene el formulario con los datos que contiene
                if form.is_valid(): 
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de mantenimiento'        
        context['list_url'] = self.success_url       
        context['action'] = 'add'        
        context['entity'] = 'Crear mantenimiento'
        context['desc'] = 'Mantenimientos y Reparaciones'
        return context              

class MantenimientoUpdateView(LoginRequiredMixin, UpdateView):# Este no tiene ajax
    model = Mantenimiento
    form_class = MantenimientoForm    
    template_name = 'mantenimiento/update_mantenimiento.html'
    success_url = reverse_lazy('gestion:mantenimiento')        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un mantenimiento'        
        context['list_url'] = self.success_url       
        context['action'] = 'edit'        
        context['entity'] = 'Editar Mantenimiento'
        context['desc'] = 'Mantenimientos y Reparaciones'
        return context  


"""
VIEWS DE LAVADO

"""

class LavadoListView(LoginRequiredMixin, ListView): #Este código funciona
    model = Lavado
    template_name = 'lavado/list_lavado.html'

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Lavado.objects.filter(usuario=self.request.user):
                    data.append(i.toJSON())     
            elif action == 'retrieveLavado':
                data = []                
                for i in Lavado.objects.filter(id=request.POST['id']):                    
                    data.append(i.toJSON())                    
            elif action == 'delete':
                m = Lavado.objects.get(pk=request.POST['id'])
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de lavados'    
        context['create_url'] = reverse_lazy('gestion:create_lavado')
        context['entity'] = 'Lavado'
        context['form'] = LavadoForm
        context['desc'] = 'Lavados'
        return context

class LavadoCreateView(LoginRequiredMixin, CreateView):
    model = Lavado
    form_class = LavadoForm    
    template_name = 'lavado/create_lavado.html'
    success_url = reverse_lazy('gestion:lavado')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):        
        return super().dispatch(request, *args, **kwargs)    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add': #esto va de acuerdo con un input hidden en el html
                form = self.get_form() #obtiene el formulario con los datos que contiene
                if form.is_valid(): 
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de lavado'        
        context['list_url'] = self.success_url       
        context['action'] = 'add'        
        context['entity'] = 'Crear lavado'
        context['desc'] = 'Lavados'
        return context              

class LavadoUpdateView(LoginRequiredMixin, UpdateView):# Este no tiene ajax
    model = Lavado
    form_class = LavadoForm    
    template_name = 'lavado/update_lavado.html'
    success_url = reverse_lazy('gestion:lavado')        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un lavado'        
        context['list_url'] = self.success_url       
        context['action'] = 'edit'        
        context['entity'] = 'Editar Lavado'
        context['desc'] = 'Lavados'
        return context  



"""
VIEWS DE RECARGA

"""
class RecargaCombustibleListView(LoginRequiredMixin, ListView): #Este código funciona
    model = RecargaCombustible
    template_name = 'recarga/list_recarga.html'

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in RecargaCombustible.objects.filter(usuario=self.request.user):
                    data.append(i.toJSON())     
            elif action == 'retrieveRecarga':
                data = []                
                for i in RecargaCombustible.objects.filter(id=request.POST['id']):                    
                    data.append(i.toJSON())                    
            elif action == 'delete':
                m = RecargaCombustible.objects.get(pk=request.POST['id'])
                m.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de recargas'    
        context['create_url'] = reverse_lazy('gestion:create_recarga')
        context['entity'] = 'Recarga'
        context['form'] = RecargaCombustibleForm
        context['desc'] = 'Recargas de combustible'
        return context

class RecargaCombustibleCreateView(LoginRequiredMixin, CreateView):
    model = RecargaCombustible
    form_class = RecargaCombustibleForm    
    template_name = 'recarga/create_recarga.html'
    success_url = reverse_lazy('gestion:recarga')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):        
        return super().dispatch(request, *args, **kwargs)    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add': #esto va de acuerdo con un input hidden en el html
                form = self.get_form() #obtiene el formulario con los datos que contiene
                if form.is_valid(): 
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Recarga de Combustible'        
        context['list_url'] = self.success_url       
        context['action'] = 'add'        
        context['entity'] = 'Crear Recarga de Combustible'
        context['desc'] = 'Recargas de combustible'
        return context              

class RecargaCombustibleUpdateView(LoginRequiredMixin, UpdateView):# Este no tiene ajax
    model = RecargaCombustible
    form_class = RecargaCombustibleForm    
    template_name = 'recarga/update_recarga.html'
    success_url = reverse_lazy('gestion:recarga')        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Recarga de Combustible'        
        context['list_url'] = self.success_url       
        context['action'] = 'edit'        
        context['entity'] = 'Editar Recarga de Combustible'
        context['desc'] = 'Recargas de combustible'
        return context  
