from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # formulario de registro
from django.contrib.auth.models import User # Modelo de usuario
from django.contrib.auth import login # Crea cookie por nosotros
from django.db import IntegrityError

# Create your views here.
def home(request):
    """Inicio"""
    return render(request, 'home.html')

def signup(request):
    """Permite registrar usuario"""
    if request.method == 'GET': # Envia formulario
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else: # Obteniendo datos del formulario
        print('obteniendo datos')
        if request.POST['password1'] == request.POST['password2']: # si contraseña1 y contraseña2 coinciden...
            try: # registrar usuario
                nombre = request.POST['username'] # Save username
                contraseña = request.POST['password1'] # Save password
                usuario = User.objects.create_user(username=nombre, password=contraseña) # create user
                usuario.save() # save user in database
                login(request, usuario) # Crea cookie en el navegador para ver si las tareas son de este usuario o no.
                return redirect('tasks') # redireccionar a tareas
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe!'
                })
        else:
            return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden!'
                })

def tasks(request):
    return render(request, 'tasks.html')