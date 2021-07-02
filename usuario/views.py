from django.shortcuts import render, redirect
from .models import Usuario, Perfil, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.db.models import Q
from django.core.validators import validate_email


def home(request):
    return render(request, 'usuario/home.html')

def teste(request):
    return render(request, 'usuario/teste.html')

def cadastro(request):
        if request.method != 'POST':
            return render(request, 'usuario/cadastro.html')

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        cidade = request.POST['cidade']
        telefone = request.POST['telefone']
        status = request.POST['status']

        if not first_name or not email or not username or not senha \
                or not senha2:
            messages.error(request, 'Preencha todos os Campos!')
            return render(request, 'usuario/cadastro.html')

        try:
            validate_email(email)
        except:
            messages.error(request, 'Email Inválido!')
            return render(request, 'usuario/cadastro.html')

        if len(senha) < 6:
            messages.error(request, 'Senha precisa ter pelo menos 6 Caracteres!')
            return render(request, 'usuario/cadastro.html')

        if senha != senha2:
            messages.error(request, 'Senhas não Correspondem!')
            return render(request, 'usuario/cadastro.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já existente para um usuário!')
            return render(request, 'usuario/cadastro.html')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'Informe outro nome de usuário!')
            return render(request, 'usuario/cadastro.html')

        messages.success(request, 'Usuário Registrado com Sucesso!')

        new_user = Usuario.objects.create_superuser(username=username, first_name=first_name, last_name=last_name,
                                                    cidade=cidade, telefone=telefone,email=email, status=status, password=senha)
        new_user.save()
        return redirect('usuario:cadastro')

def submit_login(request):
    if request.method != 'POST':
        return render(request, 'usuario/submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, 'Login Efetuado Sucesso!')
        return redirect('usuario:teste')
    messages.error(request, 'E-mail e/ou senha inválido!')
    return redirect('usuario:submit_login')




