from django.forms import *
from .models import *

class MarcaVehiculoForm(ModelForm):    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = MarcaVehiculo   
        fields = ['nombre']
        widgets = {
            'nombre' : TextInput(attrs={
                'class':'form-control mb-2',
                'placeholder':'Marca',                
            })
        } 