from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

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
