from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'esconder_botoes': True})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            return HttpResponse("Email ou Senha inválidos.")
        
def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')