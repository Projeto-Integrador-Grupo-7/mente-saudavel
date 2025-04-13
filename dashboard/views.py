from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

class Filtros:
    def __init__(self, data_inicio=None, data_fim=None, sexo=None, idade=None):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.sexo = sexo
        self.idade = idade

@login_required
def dashboard(request):

    filtros = get_filtros(request)

    grafico_dados = get_grafico_dados()
    historico_dados = get_historico(filtros)

    return render(request, 'dashboard.html', {
        'grafico_dados': grafico_dados,
        'historico_dados': historico_dados,
        'filtros': filtros
    })

def get_filtros(request):
    data_inicio = request.GET.get('dataInicio')
    data_fim = request.GET.get('dataFim')
    sexo = request.GET.get('sexo')
    idade = request.GET.get('idade')

    return Filtros(data_inicio=data_inicio, data_fim=data_fim, sexo=sexo, idade=idade)

def filtrar_historico(filtros, historico):
    data_inicio = filtros.data_inicio
    data_fim = filtros.data_fim
    
    if data_inicio:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        historico = [h for h in historico if datetime.strptime(h['data'], '%Y-%m-%d') >= data_inicio]

    if data_fim:
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        historico = [h for h in historico if datetime.strptime(h['data'], '%Y-%m-%d') <= data_fim]

    # if sexo:
    #     historico = [h for h in historico if h.get('sexo') == sexo]

    # if idade:
    #     idade = int(idade)
    #     historico = [h for h in historico if h.get('idade') == idade]

    return historico


def get_grafico_dados():
    valores = [50, 600, 200, 150]
    grafico_dados = {
        'descricao': ['Sofrimento Grave', 'Sofrimento Moderado', 'Sofrimento Leve', 'Sem Sofrimento'],
        'valores': valores,
        'participantes': sum(valores)
    }
    return grafico_dados


def get_historico(filtros):
    historico = [
        {
            'estratificacao': 'Sofrimento Grave',
            'pontuacao': 20,
            'data': '2015-12-10'
        },
        {
            'estratificacao': 'Sofrimento Leve',
            'pontuacao': 5,
            'data': '2024-09-15'
        }, 
        {
            'estratificacao': 'Sofrimento Leve',
            'pontuacao': 2,
            'data': '2025-04-02'
        },
        {
            'estratificacao': 'Sofrimento Moderado',
            'pontuacao': 8,
            'data': '2022-07-05'
        },
        {
            'estratificacao': 'Sofrimento Moderado',
            'pontuacao': 14,
            'data': '2020-01-20'
        },
    ]

    historico = filtrar_historico(filtros, historico)

    historico_ordenado = sorted(
        historico,
        key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d'),
        reverse=True
    )

    return historico_ordenado