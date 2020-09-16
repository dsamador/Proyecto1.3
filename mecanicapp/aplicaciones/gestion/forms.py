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


class LavaderoForm(Establecimiento):                
    
    class Meta(Establecimiento.Meta):
        model = Lavadero


class TallerForm(Establecimiento):                
    
    class Meta(Establecimiento.Meta):
        model = Taller


class VehiculoForm(ModelForm):

    def __init__(self, request, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
        
        self.fields['nombre'].widget.attrs['autofocus'] = True        
              
        self.fields['tipo'].empty_label = "Seleccione un tipo vehículo"
        self.fields['marca'].empty_label = "Seleccione una marca"        


    class Meta:
        model = Vehiculo
        exclude = ['usuario']
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'Ej: "Mi pichirilo"'
            }),
            'modelo' : TextInput(attrs={                  
                'placeholder':'Ej: Escarabajo'            
            }),
            'placa' : TextInput(attrs={                              
                'placeholder':'Ej: ABC123'            
            }),
            'anio' : TextInput(attrs={                               
                'placeholder':'Digite el año de su vehículo'            
            }),           
            'color' : TextInput(attrs={                                
                'placeholder':'color'            
            }),
            'tanque' : NumberInput(attrs={                               
                'placeholder':'Digite el número de galones'            
            }),
            'num_chasis' : TextInput(attrs={                   
                'placeholder':'numero del chasis'                     
            }),
            'VIN' : TextInput(attrs={                
                'placeholder':'VIN'                        
            }),
            'matricula' : TextInput(attrs={                
                'placeholder':'matricula'            
            })                          
        }        


class MantenimientoForm(ModelForm):

    def __init__(self, request, *args, **kwargs):
        super(MantenimientoForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
        
        self.fields['valor'].widget.attrs['autofocus'] = True

        self.fields['vehiculo'].queryset = Vehiculo.objects.filter(usuario=request.user)
        self.fields['taller'].queryset = Taller.objects.filter(usuario=request.user)
        self.fields['tipo_mantenimiento'].queryset = TipoMantenimiento.objects.filter(usuario=request.user)

        self.fields['vehiculo'].empty_label = "Seleccione un vehículo"
        self.fields['taller'].empty_label = "Seleccione un taller"
        self.fields['tipo_mantenimiento'].empty_label = "Seleccione un tipo de mantenimiento"

    class Meta:
        model = Mantenimiento
        exclude = ['fecha']
        widgets = {
            'valor' : NumberInput(attrs={                
                'placeholder':'máximo 11 dígitos y 2 decimales'                         
            }),            
            'nota':Textarea(attrs={
                'rows': '3',
                'placeholder':'Describa cómo fue su experiencia'
            }),             
        }

class LavadoForm(ModelForm):

    def __init__(self, request, *args, **kwargs):
        super(LavadoForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
        
        self.fields['valor'].widget.attrs['autofocus'] = True

        self.fields['vehiculo'].queryset = Vehiculo.objects.filter(usuario=request.user)
        self.fields['lavadero'].queryset = Lavadero.objects.filter(usuario=request.user)
        self.fields['tipo_lavado'].queryset = TipoLavado.objects.filter(usuario=request.user)

        self.fields['vehiculo'].empty_label = "Seleccione un vehículo"
        self.fields['lavadero'].empty_label = "Seleccione un lavadero"
        self.fields['tipo_lavado'].empty_label = "Seleccione un tipo de lavado"

    class Meta:
        model = Lavado
        exclude = ['fecha', 'usuario']
        widgets = {
            'valor' : NumberInput(attrs={                
                'placeholder':'máximo 11 dígitos y 2 decimales'                         
            }),                                    
            'nota':Textarea(attrs={
                'rows': '3',
                'placeholder':'Describa cómo fue su experiencia'
            }),            
        }

class RecargaCombustibleForm(ModelForm):

    def __init__(self, request, *args, **kwargs):
        super(RecargaCombustibleForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
        
        self.fields['cantidad'].widget.attrs['autofocus'] = True

        self.fields['vehiculo'].queryset = Vehiculo.objects.filter(usuario=request.user)
        self.fields['gasolinera'].queryset = Gasolinera.objects.filter(usuario=request.user)
        

        self.fields['vehiculo'].empty_label = "Seleccione un vehículo"
        self.fields['gasolinera'].empty_label = "Seleccione una gasolinera"
        self.fields['tipo_combustible'].empty_label = "Seleccione un tipo de combustible"
    
    class Meta:
        model = RecargaCombustible
        exclude = ['fecha']
        widgets = {
            'cantidad' : NumberInput(attrs={                
                'placeholder':'digite un número entero'                         
            }),
            'precio_galon' : NumberInput(attrs={                
                'placeholder':'máximo 11 dígitos y 2 decimales'                         
            }),
            'costo_total' : NumberInput(attrs={                
                'placeholder':'máximo 11 dígitos y 2 decimales'                         
            }),                        
            'nota':Textarea(attrs={
                'rows': '3',
                'placeholder':'Describa cómo fue su experiencia'
            }),
            'kilometraje' : NumberInput(attrs={
                'placeholder':'Digite su última lectura de odómetro'
            }),            
        }

class SelectForm(Form):
    vehiculos = ModelChoiceField(queryset=Vehiculo.objects.all(), widget=Select(attrs={
        'class':'form-control'
    }))