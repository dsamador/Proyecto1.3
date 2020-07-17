"""from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, TemplateView
from .models import User
from .forms import FormularioLogin, FormularioUser

class Login(FormView):
    template_name = 'usuario/login2.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('gestion:inicio_app')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RegistroExitoso(TemplateView):
    template_name = "usuario/registro_exitoso.html"


class RegistrarUsuario(CreateView):
    model = User
    form_class = FormularioUser
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('exito') """