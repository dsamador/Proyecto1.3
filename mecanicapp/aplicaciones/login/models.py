from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#Con esta función se borra la imágen anterior
def custom_upload_to(instance, filename):
    old_instance =  Perfil.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=  True, blank = True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['user']

    def __str__(self):        
        return f'Usuario: {self.user}'

#Creación de señal, sirve para crear el perfil apenas se crea el usuario
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(user=instance)        