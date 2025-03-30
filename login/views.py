from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario

def login(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            return HttpResponse(f"Bem-vindo(a), {usuario.nome}!")
        
        except Usuario.DoesNotExist:
            return HttpResponse("Email ou Senha inválidos.")