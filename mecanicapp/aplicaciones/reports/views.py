from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.http import JsonResponse
from aplicaciones.gestion.models import Mantenimiento, Lavado, RecargaCombustible

class ReportMantenimiento(TemplateView):
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
                search = Mantenimiento.objects.filter(usuario = self.request.user)
                if len(start_date) and len(end_date):
                    search = search.filter(fecha__range=[start_date, end_date])            

                for s in search:                    
                    data.append([                        
                        s.fecha.strftime('%Y-%m-%d'),
                        s.vehiculo.nombre,
                        s.tipo_mantenimiento.nombre,                        
                        s.taller.nombre,
                        s.razon,
                        s.valor
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


class ReportRecarga(TemplateView):
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
                search = RecargaCombustible.objects.filter(usuario = self.request.user)
                if len(start_date) and len(end_date):
                    search = search.filter(fecha__range=[start_date, end_date])            

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


class ReportLavado(TemplateView):
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
                search = Lavado.objects.filter(usuario = self.request.user)
                if len(start_date) and len(end_date):
                    search = search.filter(fecha__range=[start_date, end_date])            

                for s in search:                    
                    data.append([                        
                        s.fecha.strftime('%Y-%m-%d'),
                        s.vehiculo.nombre,
                        s.tipo_lavado.nombre,                        
                        s.lavadero.nombre,                        
                        s.valor
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
    