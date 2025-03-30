from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuario.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')

        usuario = Usuario(
            nome=nome,
            senha=senha,
            email=email,
            data_nascimento=data_nascimento,
            sexo=sexo
        )

        usuario.save()

        return HttpResponse(nome)