from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.http import JsonResponse
from aplicaciones.gestion.models import Mantenimiento, Lavado, RecargaCombustible
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportMantenimiento(LoginRequiredMixin, TemplateView):
    template_name = 'report_mant.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  

    def post(self, request, *args, **kwargs):
        data = {}              
        try:                         
            action = request.POST['action']                                  
            if action == 'search_report':                
                data = []                            
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')                
                if len(start_date) and len(end_date):
                    search = Mantenimiento.objects.only('fecha','vehiculo','tipo_mantenimiento',
                                                        'taller','razon','valor').filter(
                                                        fecha__range=[start_date, end_date],
                                                        usuario = self.request.user)                
                
                for s in search:                                        
                    data.append([                        
                        s.fecha.strftime('%Y-%m-%d'),
                        s.vehiculo.nombre,
                        s.tipo_mantenimiento.nombre,                        
                        s.taller.nombre,
                        s.razon,
                        s.valor
                    ]) 
                    
                
                total = search.aggregate(r=Coalesce(Sum('valor'),0)).get('r')
                cant = search.aggregate(r=Coalesce(Count('valor'),0)).get('r')
                
                if total and cant != 0:
                    promedio = total/cant
                else:
                    promedio = 0

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    'Total',
                    format(total, '.2f'),
                ], )

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    'Promedio',
                    format(promedio, '.2f'),
                ])

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de los mantenimientos'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reporte_mantenimientos')        
        context['form'] = ReportForm()        
        return context


class ReportRecarga(LoginRequiredMixin, TemplateView):
    template_name = 'report_recar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  

    def post(self, request, *args, **kwargs):
        data = {}              
        try:                         
            action = request.POST['action']                                  
            if action == 'search_report':                
                data = []                            
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')                                
                if len(start_date) and len(end_date):
                    search = RecargaCombustible.objects.only('fecha','cantidad','vehiculo',
                                                        'kilometraje','tipo_combustible','gasolinera','costo_total').filter(
                                                        fecha__range=[start_date, end_date],
                                                        usuario = self.request.user)          

                for s in search:                    
                    data.append([                        
                        s.fecha.strftime('%Y-%m-%d'),
                        s.cantidad,             
                        s.vehiculo.nombre,                        
                        s.kilometraje,
                        s.tipo_combustible.nombre,
                        s.gasolinera.nombre,
                        s.costo_total
                    ])                  

                total = search.aggregate(r=Coalesce(Sum('costo_total'),0)).get('r')
                cant = search.aggregate(r=Coalesce(Count('costo_total'),0)).get('r')
                
                if total and cant != 0:
                    promedio = total/cant
                else:
                    promedio = 0

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',                    
                    'Total',
                    format(total, '.2f'),
                ], )

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',
                    'Promedio',
                    format(promedio, '.2f'),
                ])
                                   
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de los recargas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reporte_recargas')
        context['form'] = ReportForm()        
        return context        


class ReportLavado(LoginRequiredMixin, TemplateView):
    template_name = 'report_lav.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  

    def post(self, request, *args, **kwargs):
        data = {}              
        try:                         
            action = request.POST['action']                                  
            if action == 'search_report':                
                data = []                            
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')                                
                if len(start_date) and len(end_date):
                    search = Lavado.objects.only('fecha','vehiculo','tipo_lavado',
                                                        'lavadero','valor').filter(
                                                        fecha__range=[start_date, end_date],
                                                        usuario = self.request.user)                       

                for s in search:                    
                    data.append([                        
                        s.fecha.strftime('%Y-%m-%d'),
                        s.vehiculo.nombre,
                        s.tipo_lavado.nombre,                        
                        s.lavadero.nombre,                        
                        s.valor
                    ])
                    
                total = search.aggregate(r=Coalesce(Sum('valor'),0)).get('r')
                cant = search.aggregate(r=Coalesce(Count('valor'),0)).get('r')
                
                if total and cant != 0:
                    promedio = total/cant
                else:
                    promedio = 0

                data.append([
                    '---',
                    '---',
                    '---',                    
                    'Total',
                    format(total, '.2f'),
                ], )

                data.append([
                    '---',
                    '---',
                    '---',                    
                    'Promedio',
                    format(promedio, '.2f'),
                ])                    
                         
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de los lavados'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reporte_lavados')
        context['form'] = ReportForm()        
        return context