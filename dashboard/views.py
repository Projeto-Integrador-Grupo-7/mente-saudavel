from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Max
from django.utils.timezone import localtime
from datetime import datetime, timedelta
from questionario.models import Formulario
from questionario.enums import Estratificacao

# region FILTROS
class Filtros:
    def __init__(self, usuario=None, data_inicio=None, data_fim=None, sexo=None, idade=None):
        self.usuario = usuario
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.sexo = sexo
        self.idade = idade
    
def get_filtros(request):
    usuario_logado=request.user
    data_inicio = request.GET.get('dataInicio')
    data_fim = request.GET.get('dataFim')
    sexo = request.GET.get('sexo')
    idade = request.GET.get('idade')

    return Filtros(usuario=usuario_logado, data_inicio=data_inicio, data_fim=data_fim, sexo=sexo, idade=idade)
# endregion

@login_required
def dashboard(request):
    filtros = get_filtros(request)

    historico_dados = get_historico(filtros)
    grafico_dados = get_grafico_dados(filtros)

    return render(request, 'dashboard.html', {
        'grafico_dados': grafico_dados,
        'historico_dados': historico_dados,
        'filtros': filtros
    })

# region HISTORICO
def filtrar_historico(historico, filtros):
    data_inicio = filtros.data_inicio
    data_fim = filtros.data_fim
    
    if data_inicio:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        historico = historico.filter(data_formulario__gte=data_inicio)

    if data_fim:
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d') + timedelta(days=1)
        historico = historico.filter(data_formulario__lte=data_fim)

    if filtros.sexo:
        historico = historico.filter(usuario__sexo=filtros.sexo)

    return historico


def get_historico(filtros):
    historico = Formulario.objects.filter(usuario=filtros.usuario)
    historico = filtrar_historico(historico, filtros)
    historico_ordenado = historico.order_by('-data_formulario')

    historico_dados = [
        {
            'id': item['id'],
            'estratificacao': Estratificacao(item['estratificacao']).nome_formatado,
            'pontuacao': item['pontuacao'],
            'data_formulario': localtime(item['data_formulario']).strftime('%d/%m/%Y %H:%M'),
        }
        for item in historico_ordenado.values('id', 'estratificacao', 'pontuacao', 'data_formulario')
    ]

    return list(historico_dados)
# endregion

# region GRAFICO
def filtrar_grafico(filtros):
    formularios = Formulario.objects.all()

    data_inicio = filtros.data_inicio
    data_fim = filtros.data_fim
    
    if data_inicio:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        formularios = formularios.filter(data_formulario__gte=data_inicio)

    if data_fim:
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d') + timedelta(days=1)
        formularios = formularios.filter(data_formulario__lte=data_fim)

    if filtros.sexo:
        formularios = formularios.filter(usuario__sexo=filtros.sexo)

    if filtros.idade:
        idade = int(filtros.idade)

        data_nascimento_max = datetime.now() - timedelta(days=idade * 365.25)
        data_nascimento_min = data_nascimento_max - timedelta(days=365.25)

        formularios = formularios.filter(
            usuario__data_nascimento__gte=data_nascimento_min,
            usuario__data_nascimento__lt=data_nascimento_max
        )

    formularios_atuais = get_ultimo_formulario_por_usuario(formularios)

    return formularios_atuais


def get_ultimo_formulario_por_usuario(formularios=None):
    if formularios is None:
        formularios = Formulario.objects.values('usuario').annotate(data_recente=Max('data_formulario'))
    else:
        formularios = formularios.values('usuario').annotate(data_recente=Max('data_formulario'))

    formularios_mais_recentes = Formulario.objects.filter(
        usuario__in=[f['usuario'] for f in formularios],
        data_formulario__in=[f['data_recente'] for f in formularios]
    )

    return formularios_mais_recentes


def get_grafico_dados(filtros):
    if any([filtros.data_inicio, filtros.data_fim, filtros.sexo, filtros.idade]):
        formularios = filtrar_grafico(filtros)
    else:
        formularios = get_ultimo_formulario_por_usuario()

    respostas = {
        Estratificacao.SOFRIMENTO_GRAVE.nome_formatado: formularios.filter(estratificacao=Estratificacao.SOFRIMENTO_GRAVE.value).count(),
        Estratificacao.SOFRIMENTO_MODERADO.nome_formatado: formularios.filter(estratificacao=Estratificacao.SOFRIMENTO_MODERADO.value).count(),
        Estratificacao.SOFRIMENTO_LEVE.nome_formatado: formularios.filter(estratificacao=Estratificacao.SOFRIMENTO_LEVE.value).count(),
        Estratificacao.NAO_IDENTIFICADO.nome_formatado: formularios.filter(estratificacao=Estratificacao.NAO_IDENTIFICADO.value).count(),
    }

    return {
        'descricao': list(respostas.keys()),
        'valores': list(respostas.values()),
        'participantes': sum(respostas.values())
    }
# endregion