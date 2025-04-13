from django.shortcuts import render, redirect
from django.urls import reverse

def questionario(request):
    return render(request, 'questionario.html')

def cadastro_questionario(request):
    if request.method == 'POST':

        pontuacao = get_pontuacao(request)

        url_resultado = f"{reverse('resultado')}?pontuacao={pontuacao}"
        return redirect(url_resultado)
    
    return render(request, 'questionario.html')

def get_pontuacao(request):
    respostas = {
        pergunta: resposta 
        for pergunta, resposta in request.POST.items()
    }
    
    pontuacao = sum(1 for resposta in respostas.values() if resposta == 'S')

    return pontuacao