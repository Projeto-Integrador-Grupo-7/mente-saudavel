from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Formulario, Resposta
from usuario.models import Usuario  # Ou seu modelo CustomUser
from django.utils import timezone

def questionario(request):
    return render(request, 'questionario.html')

def cadastro_questionario(request):
    if request.method == 'POST':
        respostas = {pergunta: resposta for pergunta, resposta in request.POST.items() if pergunta.startswith('q')}
        pontuacao = sum(1 for resposta in respostas.values() if resposta == 'S')

        # Cria o Formulário
        formulario = Formulario.objects.create(
            usuario=request.user,  # Aqui precisa estar logado! Se não quiser obrigatório, avisa que ajustamos
            pontuacao=pontuacao,
            estratificacao=0,  # Você pode calcular a estratificação depois, se quiser
            data_formulario=timezone.now()
        )

        # Salva as respostas
        for numero, valor in respostas.items():
            numero_int = int(numero[1:])  # Remove o 'q' do começo ('q1' -> 1)
            Resposta.objects.create(
                formulario=formulario,
                numero=numero_int,
                valor=1 if valor == 'S' else 0  # Valor como tinyint: 1 para 'S', 0 para 'N'
            )

        # Redireciona para a página de resultado com a pontuação
        url_resultado = f"{reverse('resultado')}?pontuacao={pontuacao}"
        return redirect(url_resultado)

    return render(request, 'questionario.html')
