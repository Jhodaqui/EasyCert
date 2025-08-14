from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import os

# Create your models here.
def contrato_upload_path(instance, filename):
    return os.path.join('contratos', f"{instance.usuario.numero_documento}", filename)

def archivo_usuario_upload_path(instance, filename):
    return os.path.join('archivos', f"{instance.usuario.numero_documento}", filename)

class Usuario(AbstractUser):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('PA', 'Pasaporte'),
    ]

    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=50, unique=True)
    fecha_inicio_constancia = models.DateField(null=True, blank=True)
    fecha_fin_constancia = models.DateField(null=True, blank=True)
    tipo_constancia = models.CharField(max_length=50, blank=True, null=True)

    ROL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('ASESOR', 'Asesor'),
        ('SUBDIR', 'Subdirector'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='ASESOR')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.numero_documento})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Contrato(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos')
    serial_contrato = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    documento_contrato = models.FileField(upload_to=contrato_upload_path, null=True, blank=True)

    def __str__(self):
        return f"{self.serial_contrato} - {self.usuario}"

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

class ArchivoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to=archivo_usuario_upload_path)
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo de {self.usuario} - {self.fecha_subida.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Archivo de Usuario"
        verbose_name_plural = "Archivos de Usuarios"