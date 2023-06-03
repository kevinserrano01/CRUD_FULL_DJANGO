from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    """Inicio"""
    return render(request, 'home.html')

def signup(request):
    """Permite registrar usuario"""
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })