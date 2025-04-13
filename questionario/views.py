from django.shortcuts import render

def questionario(request):
    return render(request, 'questionario.html')

def cadastro_questionario(request):
    if request.method == 'POST':
        return render(request, 'questionario.html')
    return render(request, 'questionario.html')