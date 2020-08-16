from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import os
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from .models import Vehiculo, Lavado
from django.utils import timezone


class AverPDF(View):
    def get(self, request, *args, **kwargs):
        try:            
            template = get_template('reports/r_vhcl.html')
            context = {
                'lavados': Lavado.objects.all(),
                'persona': {'nombre':'David'}
                #'lavados': Lavado.objects.filter(vehiculo__id=request.GET.get())
            }
            html = template.render(context)
            response = HttpResponse(content_type = 'application/pdf')
            #La linea de abajo causa que se baje el pdf automáticamente
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(html, dest = response)            
            return response    
        except:
            return HttpResponseRedirect(reverse_lazy('gestion:vehiculo'))
        

#http://127.0.0.1:8000/app/lavados/pdf/1/