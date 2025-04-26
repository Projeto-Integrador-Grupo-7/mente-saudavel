from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import Formulario, Resposta
from questionario.enums import Estratificacao

@login_required
def questionario(request):
    if request.method == 'GET':
        return render(request, 'questionario.html')
    
    try:
        respostas = {pergunta: resposta for pergunta, resposta in request.POST.items() if pergunta.startswith('q')}
        pontuacao = sum(1 for resposta in respostas.values() if resposta == 'S')

        formulario = Formulario.objects.create(
            usuario=request.user,
            pontuacao=pontuacao,
            estratificacao=get_estratificacao(pontuacao),
            data_formulario=timezone.now()
        )

        for numero, valor in respostas.items():
            numero_int = int(numero[1:])
            Resposta.objects.create(
                formulario=formulario,
                numero=numero_int,
                valor=1 if valor == 'S' else 0
            )

        url_resultado = f"{reverse('resultado')}?pontuacao={pontuacao}"
        return redirect(url_resultado)
    
    except Exception:
        return render(request, 'questionario.html', {
            'error': 'Não foi possível submeter o questionário.'
        })

def get_estratificacao(pontuacao):
    if pontuacao >= 15:
        return Estratificacao.SOFRIMENTO_GRAVE.value
    elif 8 <= pontuacao <= 14:
        return Estratificacao.SOFRIMENTO_MODERADO.value
    elif 1 <= pontuacao <= 7:
        return Estratificacao.SOFRIMENTO_LEVE.value
    else:
        return Estratificacao.NAO_IDENTIFICADO.value