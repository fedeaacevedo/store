from django.http import HttpResponse
from django.shortcuts import render

from django.contrib import auth

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

    return render(request, 'usuarios/login.html', {

    })    