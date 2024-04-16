from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class TipoMascota(models.Model):
    id =models.IntegerField(primary_key=True,verbose_name='Id')
    TipoMascota = models.CharField(max_length=50, verbose_name='Gato/Perro')

    def __str__(self):
        return self.TipoMascota
    
class Producto(models.Model):
    url = models.CharField(max_length=150, null=False, blank=False)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    imagen = models.ImageField(upload_to=get_file_path, null=True, blank= False)
    descripcion = models.CharField(max_length=1500, null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.FloatField(null=False, blank=False)
    precioOferta = models.FloatField(null=False, blank=True, default=0)
    status = models.BooleanField(default=False, help_text="0=inhabilitado, 1 habilitado")
    tag = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre