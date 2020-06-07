from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from .models import MarcaVehiculo
from .forms import MarcaVehiculoForm

from django.http import JsonResponse

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        return context


""" class MarcaView(ListView):    
    model = MarcaVehiculo
    template_name = 'marca/list_marca.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name':'David'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de marcas'        
        return context """

"""
    Vistas de las marcas de vehiculos
"""

class MarcaView(TemplateView):    
    template_name = 'marca/list_marca.html'    
    
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
        #context['create_url'] = reverse_lazy('gestion:crear_marca')
        #context['list_url'] = reverse_lazy('gestion:listar_marcas')
        context['entity'] = 'Marca'
        context['form'] = MarcaVehiculoForm()
        return context 



