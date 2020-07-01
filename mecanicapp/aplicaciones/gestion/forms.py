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

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class OdometroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['distancia'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Odometro
        fields = '__all__'
        widgets = {
            'distancia' : NumberInput(attrs={                
                'placeholder':'Distancia',
            }),
            'vehiculo' : Select(attrs={                
                'placeholder':'Vehiculo'                
            }),
        }

class VehiculoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2 bg-dark'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Vehiculo
        exclude = ['usuario']
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'nombre del carro'
            }),
            'modelo' : TextInput(attrs={                  
                'placeholder':'modelo'            
            }),
            'placa' : TextInput(attrs={                              
                'placeholder':'placa'            
            }),
            'anio' : TextInput(attrs={                               
                'placeholder':'año'            
            }),           
            'color' : TextInput(attrs={                                
                'placeholder':'color'            
            }),
            'tanque' : NumberInput(attrs={                               
                'placeholder':'capacidad del tanque'            
            }),
            'num_chasis' : TextInput(attrs={                   
                'placeholder':'numero del chasis'                     
            }),
            'VIN' : TextInput(attrs={                
                'placeholder':'VIN'                        
            }),
            'matricula' : TextInput(attrs={                
                'placeholder':'matricula'            
            }),
            'tipo' : Select(attrs={                           
                'placeholder':'tipo de vehiculo'            
            }),
            'marca' : Select(attrs={                
                'placeholder':'marca'                         
            }),               
        }        


class MantenimientoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
            self.fields['valor'].widget.attrs['autofocus'] = True

    class Meta:
        model = Mantenimiento
        exclude = ['fecha']
        widgets = {
            'valor' : NumberInput(),
            'vehiculo': Select(),
            'local':Select(),
            'tipo_mantenimiento': Select(),
            'nota':Textarea(attrs={
                'rows': '3'
            }),            
        }

class LavadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
            self.fields['valor'].widget.attrs['autofocus'] = True

    class Meta:
        model = Lavado
        exclude = ['fecha']
        widgets = {
            'valor' : NumberInput(),
            'vehiculo': Select(),
            'local':Select(),
            'tipo_lavado': Select(),
            'nota':Textarea(attrs={
                'rows': '3'
            }),            
        }

class RecargaCombustibleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
            self.fields['cantidad'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = RecargaCombustible
        exclude = ['fecha']
        widgets = {
            'cantidad' : NumberInput(),
            'precio_galon' : NumberInput(),
            'costo_total' : NumberInput(),            
            'vehiculo': Select(),            
            'tipo_combustible': Select(),
            'gasolinera':Select(),
            'nota':Textarea(attrs={
                'rows': '3'
            }),
            
        }

class SelectForm(Form):
    vehiculos = ModelChoiceField(queryset=Vehiculo.objects.all(), widget=Select(attrs={
        'class':'form-control'
    }))