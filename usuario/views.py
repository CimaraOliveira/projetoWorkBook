from django.shortcuts import render, redirect
from .models import Usuario, Perfil, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .form import FormPerfil
from django.core.validators import validate_email


def home(request):
    return render(request, 'usuario/home.html')

def teste(request):
    return render(request, 'usuario/teste.html')

def index(request):
    return render(request, 'usuario/index.html')

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
        return redirect('usuario:home')

def add_perfil(request):
    form = FormPerfil(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.success(request, 'Perfil Adicionado com sucesso!')
        return redirect('usuario:add_perfil')
    else:
        form = FormPerfil(request.POST, request.FILES)
    context = {
        'form': form
    }
    return render(request, 'usuario/add_perfil.html',context)

"""def categorias(request):
    categoria = Categoria.objects.all()

    context = {
        'categoria': categoria
    }
    return render(request, 'usuario/teste.html', context)"""

def categoria(request):
    categorias = []
    for key, value in request.POST.items():
        if key.find('categoria') >= 0:
            print(key, value)
            categoria = Categoria.objects.get(id=value)
            if categoria:
                categorias.append(categoria)
    return categorias



"""def perfil(request): //


    if request.method != 'POST':
        return render(request, 'usuario/add_perfil.html')

    profissao = request.POST['profissao']
    categoria = request.POST['categoria']
    descricao = request.POST['descricao']
    imagem = request.POST['imagem']
    cidade = request.POST['cidade']
    user = request.POST['user']
    return render(request, 'usuario/add_perfil.html')
"""
def submit_login(request):
    if request.method != 'POST':
        return render(request, 'usuario/submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, 'Login Efetuado Sucesso!')
        return redirect('usuario:index')
    messages.error(request, 'E-mail e/ou senha inválido!')
    return redirect('usuario:submit_login')


def logout_user(request):
    request.session.flush()
    logout(request)
    return redirect('usuario:home')

