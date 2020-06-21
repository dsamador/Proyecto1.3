from django.db import models
from django.conf import settings
from django_userforeignkey.models.fields import UserForeignKey
from aplicaciones.user.models import User
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL

# Create your models here

class Comunes(models.Model):
    nombre = models.CharField('Nombre (obligatorio)',max_length=200, blank=False, null=False) # El verbose name se combierte en label en el html
    descripcion = models.TextField('Descripción (opcional)',blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        abstract = True

class TipoLavado(Comunes):   

    class Meta:
        verbose_name = 'Tipo de lavado'
        verbose_name_plural = 'Tipos de lavados'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class TipoMantenimiento(Comunes):    
    
    class Meta:
        verbose_name = 'Tipo Mantenimiento'
        verbose_name_plural = 'Tipos de Mantenimientos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Gasolinera(Comunes):
    
    direccion = models.CharField('Dirección (opcional)', max_length=250, blank=True, null=True)

    class Meta:        
        verbose_name = 'Gasolinera'
        verbose_name_plural = 'Gasolineras'

    def __str__(self):        
        return self.nombre


class Local(Comunes):    
    direccion = models.CharField('Dirección (opcional)', max_length=250, blank=True, null=True)    

    class Meta:        
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):        
        return self.nombre

class TipoCombustible(models.Model):
    """Model definition for TipoCombustible."""
    nombre = models.CharField('Nombre', max_length=40, unique = True, blank=False, null=False)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Meta definition for TipoCombustible."""

        verbose_name = 'Tipo de Combustible'
        verbose_name_plural = 'Tipos de Combustibles'
        ordering = ['nombre']

    def __str__(self):
        """Unicode representation of TipoCombustible."""
        return self.nombre


class MarcaVehiculo(models.Model):
    """Model definition for MarcaVehiculo."""
    nombre = models.CharField('Nombre de la marca', unique = True, max_length=40, blank=False, null=False)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Meta definition for MarcaVehiculo."""

        verbose_name = 'Marca del Vehiculo'
        verbose_name_plural = 'Marcas de los Vehiculos'
        ordering = ['nombre']

    def __str__(self):
        """Unicode representation of MarcaVehiculo."""
        return self.nombre
        

class TipoVehiculo(models.Model):
    """Model definition for TipoVehiculo."""
    nombre = models.CharField('Tipo de vehículo', unique = True, max_length=50, blank=False, null=False)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
        
    class Meta:
        """Meta definition for TipoVehiculo."""

        verbose_name = 'Tipo de Vehiculo'
        verbose_name_plural = 'Tipos de Vehiculos'
        ordering = ['nombre']

    def __str__(self):
        """Unicode representation of TipoVehiculo."""
        return self.nombre


class Vehiculo(models.Model):
    """Model definition for Vehiculo."""
    nombre = models.CharField('Nombre del vehículo', max_length=100, blank=False, null=False)
    modelo = models.CharField('Modelo', max_length=100, blank=False, null=False)
    placa = models.CharField('Placa', unique=True, max_length=15, blank=False, null=False)
    anio = models.CharField('Año', max_length=4, blank=False, null=False)    
    color = models.CharField('Color', max_length=40, blank=True, null=True)
    tanque = models.IntegerField('Capacidad Tanque', blank=False, null=False)
    num_chasis = models.CharField('Numero del Chasis', unique=True, max_length=100, blank=True, null=True)
    VIN = models.CharField('VIN', unique=True, max_length=45, blank=True, null=True)
    matricula = models.CharField('Matrícula', unique=True, max_length=45, blank=True, null=True)
    tipo = models.ForeignKey(TipoVehiculo, on_delete = models.CASCADE)
    marca = models.ForeignKey(MarcaVehiculo, on_delete = models.CASCADE)
    usuario = UserForeignKey(auto_user_add=True,related_name='+',verbose_name="Dueño")
    imagen = models.ImageField('Imagen del vehiculo', upload_to='vehiculos', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['tipo'] = self.tipo.toJSON()
        item['marca'] = self.marca.toJSON()
        item['imagen'] = self.get_imagen()
        return item

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:        
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):        
        return self.nombre

class Odometro(models.Model):    
    distancia = models.PositiveIntegerField(blank=False, null=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete = models.CASCADE, default=None)
    fecha = models.DateTimeField('Fecha',auto_now=True)

    def toJSON(self):
        item = model_to_dict(self)
        item['vehiculo'] = self.vehiculo.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:        
        verbose_name = 'Odómetro'
        verbose_name_plural = 'Odómetros'
        #unique_together = ('vehiculo', 'distancia') Me da problemas

    def __str__(self):        
        return f'Vehículo : {self.vehiculo}, distancia : {self.distancia}, fecha : {self.fecha}'


class Servicio(models.Model):
    fecha = models.DateTimeField('Fecha de servicio',auto_now_add=True)
    valor = models.DecimalField('Valor', max_digits=11, decimal_places=2, blank=False, null=False)    
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=False, null=False)
    nota = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Lavado(Servicio):
    """Model definition for Lavado."""
    tipo_lavado = models.ForeignKey(TipoLavado, on_delete=models.CASCADE)
    comprobante = models.ImageField(upload_to="recibos_lavados/%Y/%m/%d", null=True, blank=True)   

    def toJSON(self):
        item = model_to_dict(self)
        item['vehiculo'] = self.vehiculo.toJSON()
        item['tipo_lavado'] = self.tipo_lavado.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['local'] = self.local.toJSON()
        item['comprobante'] = self.get_imagen()
        return item

    def get_imagen(self):
        if self.comprobante:
            return '{}{}'.format(MEDIA_URL, self.comprobante)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    class Meta:
        """Meta definition for Lavado."""

        verbose_name = 'Lavado'
        verbose_name_plural = 'Lavados'
        ordering = ['fecha']

    def __str__(self):
        """Unicode representation of Lavado."""
        return f'{self.tipo_lavado}, Fecha: {self.fecha}'


class Mantenimiento(Servicio):    
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)    
    comprobante = models.ImageField(upload_to="recibos_matenimientos/%Y/%m/%d", null=True, blank=True)     

    def toJSON(self):
        item = model_to_dict(self)
        item['vehiculo'] = self.vehiculo.toJSON()
        item['tipo_mantenimiento'] = self.tipo_mantenimiento.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['local'] = self.local.toJSON()
        item['comprobante'] = self.get_imagen()
        return item

    def get_imagen(self):
        if self.comprobante:
            return '{}{}'.format(MEDIA_URL, self.comprobante)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:        
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        ordering=['fecha']

    def __str__(self):        
        return f'{self.tipo_mantenimiento}, Fecha: {self.fecha}'


class RecargaCombustible(models.Model):        
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)
    precio_galon = models.DecimalField('Precio del galón', max_digits=11, decimal_places=2)
    costo_total = models.DecimalField('Costo del servicio', max_digits=11, decimal_places=2)
    comprobante = models.ImageField(upload_to="recibos_recargas/%Y/%m/%d", null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)    
    gasolinera = models.ForeignKey(Gasolinera, on_delete=models.CASCADE, default = None)    
    nota = models.TextField(blank=True, null=True)   

    def toJSON(self):
        item = model_to_dict(self)
        item['vehiculo'] = self.vehiculo.toJSON()
        item['tipo_combustible'] = self.tipo_combustible.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['gasolinera'] = self.gasolinera.toJSON()
        item['comprobante'] = self.get_imagen()
        return item

    def get_imagen(self):
        if self.comprobante:
            return '{}{}'.format(MEDIA_URL, self.comprobante)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Recarga de Combustible'
        verbose_name_plural = 'Recargas de Combustibles'
        ordering=['fecha']

    def __str__(self):    
        return f'Costo: {self.costo_total}, Fecha: {self.fecha}'