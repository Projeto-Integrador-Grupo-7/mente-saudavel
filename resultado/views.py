from django.shortcuts import render
from questionario.enums import Estratificacao

def resultado(request):
    pontuacao = request.GET.get('pontuacao', 0)
    estratificacao_value = int(request.GET.get('estratificacao', 0))

    estratificacao = Estratificacao(estratificacao_value).nome_formatado

    enum_estratificacao = {e.name: e.nome_formatado for e in Estratificacao}

    return render(request, 'resultado.html', {
        'pontuacao': pontuacao,
        'estratificacao': estratificacao,
        'enum_estratificacao': enum_estratificacao
    })