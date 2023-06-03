from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # formulario de registro
from django.contrib.auth.models import User # Modelo de usuario
from django.http import HttpResponse

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
            try:
                # registrar usuario
                nombre = request.POST['username'] # Save username
                contraseña = request.POST['password1'] # Save password
                usuario = User.objects.create_user(username=nombre, password=contraseña) # create user
                usuario.save() # save user in database
                return HttpResponse('Usuario creado exitosamente!')
            except:
                return HttpResponse('El usuario ya existe...')
        else:
            return HttpResponse('contraseñas no coinciden!')