from django.shortcuts import render

def resultado(request):
    pontuacao = request.GET.get('pontuacao')
    return render(request, 'resultado.html', {'pontuacao': pontuacao})
