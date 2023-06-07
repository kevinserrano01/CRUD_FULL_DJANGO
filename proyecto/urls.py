from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls), # Admin
    path('', views.home, name='home'), # Pagina Principal
    path('signup/', views.signup, name='signup'), # Registrarse
    path('tasks/', views.tasks, name='tasks'), # lista tareas
    path('logout/', views.signout, name='logout'), # Cerrar Sesion
    path('signin/', views.signin, name='signin'), # Iniciar Sesion
]
