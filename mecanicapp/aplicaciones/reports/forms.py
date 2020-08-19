from django.forms import *

class ReportForm(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class':'form-control',
        'autocomplete':'off'
    }))   

    
    """ TABLAS_CHOICES=(
        ('0','Seleccione aquí una tabla'),
        ('1', 'MANTENIMIENTOS'),
        ('2', 'RECARGAS'),
        ('3', 'LAVADOS')
    )
    
    tabla = ChoiceField(choices = TABLAS_CHOICES,widget=Select(attrs={'class':'form-control','autocomplete':'off'}))
 """


   