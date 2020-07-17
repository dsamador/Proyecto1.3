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
    
    email = EmailField(required = True, help_text = "Requerido, 254 caracteres como máximo y debe ser válido") 
    
    class Meta(UserCreationForm):
        model = User        
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email