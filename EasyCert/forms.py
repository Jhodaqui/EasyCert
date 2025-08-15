from django import forms
from .models import Usuario, Contrato, ArchivoUsuario

class RegistroUsuarioForm(forms.ModelForm):
    # Campos con los mismos name="" que usa tu main.html
    nombre = forms.CharField(max_length=255, label="Nombre Completo")
    documento = forms.CharField(max_length=50, label="Número Documento")
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'documento',
            'tipo_documento',
            'email',
            'fecha_inicio',
            'fecha_fin',
            'tipo_constancia',
        ]

    def save(self, commit=True):
        usuario = super().save(commit=False)

        # Separar el nombre en first_name y last_name
        nombre_completo = self.cleaned_data['nombre'].strip()
        partes = nombre_completo.split(' ', 1)
        usuario.first_name = partes[0]
        usuario.last_name = partes[1] if len(partes) > 1 else ''

        # Mapear campos a los reales del modelo
        usuario.numero_documento = self.cleaned_data['documento']
        usuario.fecha_inicio_constancia = self.cleaned_data['fecha_inicio']
        usuario.fecha_fin_constancia = self.cleaned_data['fecha_fin']

        if commit:
            usuario.save()
        return usuario

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = [
            'usuario',
            'serial_contrato',
            'fecha_inicio',
            'fecha_fin',
            'documento_contrato',
        ]
        labels = {
            'usuario': 'Usuario',
            'serial_contrato': 'Serial del contrato',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de fin',
            'documento_contrato': 'Documento del contrato',
        }

class ArchivoUsuarioForm(forms.ModelForm):
    class Meta:
        model = ArchivoUsuario
        fields = [
            'usuario',
            'archivo',
            'descripcion',
        ]
        labels = {
            'usuario': 'Usuario',
            'archivo': 'Archivo',
            'descripcion': 'Descripción',
        }
