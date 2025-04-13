from django.shortcuts import render
from django.shortcuts import redirect

def questionario(request):
    return render(request, 'questionario.html')

def cadastro_questionario(request):
    if request.method == 'POST':
        return redirect('resultado')
    return render(request, 'questionario.html')