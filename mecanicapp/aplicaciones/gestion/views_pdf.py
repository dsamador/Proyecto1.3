from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse, JsonResponse


class AverPDF(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('aver')