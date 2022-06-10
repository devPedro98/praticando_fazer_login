from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    return render(request, 'fazerlogin/html/modelo.html')


def login_user(request):
    return render(request, 'fazerlogin/html/formulario2.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def ola(request):
    return render(request, 'fazerlogin/html/teste.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return redirect('/')
