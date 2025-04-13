from django.shortcuts import render

def resultado(request):
    pontuacao = request.GET.get('pontuacao', 0)
    return render(request, 'resultado.html', {'pontuacao': pontuacao})
