from django.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm #Formulario que trae django por defecto
from django.contrib.auth.models import User
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
    
    #email único
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email

    #username único
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El username ya está registrado, prueba con otro")
        return username


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'link', 'avatar']
        widgets = {
            'avatar': ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': Textarea(attrs={'class':'form-control mt-3 mb-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': URLInput(attrs={'class':'form-control mb-3', 'placeholder':'Enlace'}),
        }

class EmailForm(ModelForm):
    email = EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        #changed_data es una lista de los campos modificados en el form
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email