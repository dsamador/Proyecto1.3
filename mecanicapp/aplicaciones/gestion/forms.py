from django.forms import *
from .models import *

class SoloNombre(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'Nombre'}),            
        } 


class MarcaVehiculoForm(SoloNombre):    
    
    class Meta(SoloNombre.Meta):
        model = MarcaVehiculo   

class TipoCombustibleForm(SoloNombre):    
    
    class Meta(SoloNombre.Meta):
        model = TipoCombustible   

class TipoVehiculoForm(SoloNombre):

    class Meta(SoloNombre.Meta):
        model = TipoVehiculo

class ComunTipo(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'Nombre'}),

            'descripcion' : Textarea(attrs={                
                'placeholder':'Descripción',
                'rows':'2'}),
        }        

class TipoLavadoForm(ComunTipo):

    class Meta(ComunTipo.Meta):
        model = TipoLavado        

class TipoMantenimientoForm(ComunTipo):                
    
    class Meta(ComunTipo.Meta):
        model = TipoMantenimiento        

class Establecimiento(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:    
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'Nombre'}),

            'direccion' : TextInput(attrs={                
                'placeholder':'Dirección'}),

            'descripcion' : Textarea(attrs={                
                'placeholder':'Descripción',
                'rows':'2'}),
        }
    
class GasolineraForm(Establecimiento):
                    
    class Meta(Establecimiento.Meta):
        model = Gasolinera

class LocalForm(Establecimiento):                
    
    class Meta(Establecimiento.Meta):
        model = Local

class OdometroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Odometro
        fields = '__all__'
        widgets = {
            'distancia' : NumberInput(attrs={                
                'placeholder':'Marca',
            }),
            'vehiculo' : Select(attrs={                
                'placeholder':'Vehiculo'                
            }),
        }