from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from .models import Vehiculo
from .forms import VehiculoForm

from django.http import JsonResponse


class VehiculoListView(ListView): #Este código funciona
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
                for i in Vehiculo.objects.all():
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
        return context


class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm    
    template_name = 'vehiculo/create.html'
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
        return context         

class VehiculoUpdateView(UpdateView):# Este no tiene ajax
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
        return context    






""" elif action == 'edit':
    m = Vehiculo.objects.get(pk=request.POST['id'])
    m.nombre = request.POST['nombre']
    m.modelo = request.POST['descripcion']
    m.placa = request.POST['placa']
    m.anio = request.POST['anio']
    m.color = request.POST['color']
    m.tanque = request.POST['tanque']
    m.num_chasis = request.POST['num_chasis']
    m.VIN = request.POST['VIN']
    m.matricula = request.POST['matricula']
    m.tipo = request.POST['tipo']
    m.marca = request.POST['marca']                
    m.save() """