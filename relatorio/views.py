from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import localtime
from questionario.models import Formulario
from questionario.enums import Estratificacao

@login_required
def relatorio(request):
    formulario_atual = get_formulario_atual(request)
    enum_estratificacao = {e.name: e.nome_formatado for e in Estratificacao}

    return render(request, 'relatorio.html', { 
        'formulario': formulario_atual, 
        'enum_estratificacao': enum_estratificacao
        })


def get_formulario_atual(request):
    formulario_atual = Formulario.objects.filter(usuario=request.user).order_by('-data_formulario').first()

    if formulario_atual:
        formulario_atual = {
            'estratificacao': Estratificacao(formulario_atual.estratificacao).nome_formatado,
            'pontuacao': formulario_atual.pontuacao,
            'data_formulario': localtime(formulario_atual.data_formulario).strftime('%d/%m/%Y %H:%M'),
        }

    return formulario_atual