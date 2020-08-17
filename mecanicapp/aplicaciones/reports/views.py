from django.shortcuts import render
from django.views.generic import TemplateView

class Report(TemplateView):
    template_name = 'report.html'
