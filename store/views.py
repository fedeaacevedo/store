from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from store.forms import RegisterForm

def index(request):
    return render(request, 'index.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #authenticate es una funcion de django, nos permite ver si existen user con ese nombre y pass
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña no valido")

    return render(request, 'usuarios/login.html', {

    })    


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       
         user = form.save()
         if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'usuarios/register.html',{
        'form': form
    })