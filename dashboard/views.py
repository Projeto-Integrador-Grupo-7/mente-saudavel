from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

@login_required
def dashboard(request):
    
    grafico_dados = get_grafico_dados()
    historico = get_historico()

    return render(request, 'dashboard.html', {
        'grafico_dados': grafico_dados,
        'historico': historico,
    })

def get_grafico_dados():
    valores = [50, 600, 200, 150]
    grafico_dados = {
        'descricao': ['Sofrimento Grave', 'Sofrimento Moderado', 'Sofrimento Leve', 'Sem Sofrimento'],
        'valores': valores,
        'participantes': sum(valores)
    }
    return grafico_dados

def get_historico():
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

    historico_ordenado = sorted(
        historico,
        key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d'),
        reverse=True
    )

    return historico_ordenado