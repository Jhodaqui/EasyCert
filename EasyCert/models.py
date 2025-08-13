from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=50, unique=True)
    fecha_inicio_constancia = models.DateField(null=True, blank=True)
    fecha_fin_constancia = models.DateField(null=True, blank=True)
    tipo_constancia = models.CharField(max_length=50)

    ROL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('ASESOR', 'Asesor'),
        ('SUBDIR', 'Subdirector'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='ASESOR')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.numero_documento})"

class Contrato(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos')
    serial_contrato = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    documento_contrato = models.FileField(upload_to='contratos/', null=True, blank=True)

    def __str__(self):
        return f"Contrato {self.serial_contrato} - {self.usuario}"

class ArchivoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='archivos/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo de {self.usuario} - {self.fecha_subida}"
