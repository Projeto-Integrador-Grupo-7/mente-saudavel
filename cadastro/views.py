from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'esconder_botoes': True})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')

        User = get_user_model()

        try:
            User.objects.create_user(
                email=email,
                password=senha,
                nome=nome,
                data_nascimento=data_nascimento,
                sexo=sexo
            )

            return redirect('login_usuario')
        
        except Exception:
            return render(request, 'cadastro.html', {
                'esconder_botoes': True,
                'error': 'Não foi possível cadastrar o usuário.'
            })