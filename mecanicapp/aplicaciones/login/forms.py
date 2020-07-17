from django.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm #Formulario que trae django por defecto
from aplicaciones.user.models import User
from django.contrib.auth.forms import UserCreationForm


class FormularioLogin(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User        
        fields = ['username', 'password1','password2']
