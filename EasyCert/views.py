from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm, ContratoForm, ArchivoUsuarioForm

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Contrato, ArchivoUsuario
from .serializers import UsuarioSerializer, ContratoSerializer, ArchivoUsuarioSerializer

# Create your views here.
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir a otra página o mostrar mensaje
            return redirect('login')
    else:
        form = RegistroUsuarioForm()

    # Renderizamos tu plantilla main.html con el formulario
    return render(request, 'main.html', {'form': form})

def registrar_contrato(request):
    if request.method == "POST":
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContratoForm()
    return render(request, 'registrar_contrato.html', {'form': form})

def subir_archivo(request):
    if request.method == "POST":
        form = ArchivoUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArchivoUsuarioForm()
    return render(request, 'subir_archivo.html', {'form': form})
# forms


# Solicitantes main

def solicitud_constancia(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        documento = request.POST.get('documento')
        tipo_documento = request.POST.get('tipo_documento')
        email = request.POST.get('email')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        tipo_constancia = request.POST.get('tipo_constancia')

        # Aquí podrías guardar en BD o procesar
        messages.success(request, 'Solicitud enviada correctamente.')
        return redirect('solicitud')

    return render(request, 'main.html')

# Login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')  # admin o asesor

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user_type == "admin":
                return redirect('/admin-dashboard/')  # ruta para admin
            elif user_type == "asesor":
                return redirect('/asesor-dashboard/')  # ruta para asesor
        else:
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'login.html')

#  views probando backends

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

class ArchivoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ArchivoUsuario.objects.all()
    serializer_class = ArchivoUsuarioSerializer
    permission_classes = [IsAuthenticated]
