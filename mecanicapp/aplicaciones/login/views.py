from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, UpdateView
from .forms import *
import config.settings as setting


class LoginFormView(LoginView):
    form_class = FormularioLogin
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

"""
    VISTA PARA REGISTRO DE USUARIOS
"""

from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class SingUpView(CreateView):
    form_class = CustomUserCreationForm
    #success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Digita aquí tu contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})

        #Borrar los campos de ayuda
        form.fields['username'].help_text = None
        form.fields['email'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

        return form 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una cuenta'
        return context

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Perfil

@method_decorator(login_required, name='dispatch')
class PerfilView(UpdateView):
    form_class = PerfilForm    
    success_url = reverse_lazy('perfil')
    template_name = 'registration/profile_form.html'    

    def get_object(self):
        #Recuperar el objeto que se va a editar
        perfil, created = Perfil.objects.get_or_create(user=self.request.user)
        return perfil

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['entity'] = 'Perfil'
        context['title'] = 'Perfil'
        context['desc'] = 'Perfil de usuario'
        return context


@method_decorator(login_required, name = 'dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm    
    success_url = reverse_lazy('perfil')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):                
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificar el form en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['entity'] = 'Cambiar email'
        context['title'] = 'Cambiar email'
        context['desc'] = 'Cambio de email'
        return context        