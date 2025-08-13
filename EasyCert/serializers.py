from rest_framework import serializers
from .models import Usuario, Contrato, ArchivoUsuario

class ArchivoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoUsuario
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, read_only=True)
    archivos = ArchivoUsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'
