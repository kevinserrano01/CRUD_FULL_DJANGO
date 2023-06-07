from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# UserCreationForm: crear un usuario. | AuthenticationForm: comprobar si un usuario ya existe.
from django.contrib.auth.models import User # Modelo de usuario
from django.contrib.auth import login, logout, authenticate # Crea cookie por nosotros
from django.db import IntegrityError


def home(request):
    """Inicio"""
    return render(request, 'home.html')

def signup(request):
    """Funcion que permite registrar usuario"""
    if request.method == 'GET': # Envia formulario
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else: # Obteniendo datos del formulario
        print('obteniendo datos de registro')
        if request.POST['password1'] == request.POST['password2']: # si contraseña1 y contraseña2 coinciden...
            try: # registrar usuario
                nombre = request.POST['username'] # Save username
                contraseña = request.POST['password1'] # Save password
                usuario = User.objects.create_user(username=nombre, password=contraseña) # create user
                usuario.save() # save user in database
                login(request, usuario) # Crea cookie en el navegador para ver si las tareas son de este usuario o no.
                return redirect('tasks') # redireccionar a tareas
            except IntegrityError: # Manejamos el error de la base de datos en caso de que ya exista un usuario
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
    """ Funcion que muestra la lista de tareas del usuario
        Returns: Redirecciona a la lista de tareas
    """
    return render(request, 'tasks.html')

def signout(request):
    """Funcion que cierra sesion en la app y lo redirecciona al home"""
    logout(request)
    return redirect('home')

def signin(request):
    """Funcion para logearse (Iniciar sesion) en la app
        Returns: Si no obtenemos datos solo recargamos el formulario, de lo contrario si recibimos, verificamos que ese user exista.
        Si existe,
    """
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        print('obteniendo datos de inicio de sesion')
        # print(request.POST) # ver que trae username and password
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # Verificar si la cuenta esta en la base de datos.
        if user is None: # Si el user esta vacio me devuelve el formulario nuevamente con un mensaje de error.
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
            })
        else: # Si el usuario y contraseña existen, guarda sesion y lo redirecciono a la lista de tareas.
            login(request, user) # Guardo sesion
            return redirect('tasks') # Redireccion a lista de tareas

        # Forma no necesaria ya que contamos con el authenticate del framework Django
        # users = User.objects.all()
        # print(users)
        # for user in users:
        #     if request.POST['username'] == user.username and request.POST['password'] == user.password:
        #         print('usuario encontrado')
        #         break
        #     else:
        #         print('user NO encontrado')