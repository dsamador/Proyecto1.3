""" from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,View
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.core import serializers
from models import *
from forms import *

def CrearTipoCombustible(request):
    data = dict()
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        tipo_combustible = TipoCombustible(nombre = nombre)
        tipo_combustible.save();
        data['nombre'] = tipo_combustible.nombre """
    