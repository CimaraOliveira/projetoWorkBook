from django.shortcuts import render, redirect
from .models import Usuario, Perfil, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.db.models import Q

def home(request):
    return render(request, 'usuario/home.html')

def register(request):
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        cidade = request.POST['cidade']
        telefone = request.POST['telefone']

        return {"username": username, "email": email, "senha": senha, "cidade": cidade, "telefone": telefone,
                "perfil": profissional(request)}

# buscar categorias pelos ids informados no html
def get_categorias(request):
    categorias = []
    for key, value in request.POST.items():
        if key.find('categoria') >= 0:
            print(key, value)
            categoria = Categoria.objects.get(id=value)
            if categoria:
                categorias.append(categoria)
    return categorias

    # Aqui controla a parte do profissional
def  profissional(request):
        if request.POST['user'] == 'profissional':
            name_prof = request.POST['profissao']
            descricao = request.POST['descricao']
            slogan = request.FILES.get('slogan')
            perfil = Perfil.objects.create(nome=name_prof, decricao=descricao, slogan=slogan)
            perfil.categorias.set(get_categorias(request))
            return perfil
        return None

def __get__register(request, user, error):
        categorias = Categoria.objects.all()
        return render(request, 'usuario/cadastro.html', {"categorias": categorias, 'user': user, 'error': error})

def cadastro(request):
        if request.method != 'POST':
            return __get__register(request, None, None)
        user_request = register(request)
        username = user_request.get('username')
        first_name = request.POST['first_name']
        email = user_request.get('email')
        senha = user_request.get('senha')
        cidade = user_request.get('cidade')
        telefone = user_request.get('telefone')
        perfil = user_request.get('perfil')
        last_name = user_request.get('last_name')

        user = {'username': username, 'first_name': first_name, 'email': email, 'senha': senha, 'telefone': telefone,
                'perfil': request.POST['user']}

        user_db = Usuario.objects.filter(email=email)

        if not user_db:
            print('success')
            messages.success(request, 'Usuário Registrado com Sucesso!')

            new_user = Usuario.objects.create_superuser(username=username, first_name=first_name, last_name=last_name,
                                                        email=email, password=senha, cidade=cidade, telefone=telefone,
                                                        perfil=perfil)
            new_user.save()
            return redirect('usuario:cadastro')
        print('error')
        return __get__register(request, user, {'error': 'Usuário já Registrado. Tente outro Usuário!'})

def submit_login(request):
    if request.method != 'POST':
        return render(request, 'usuario/submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        messages.success(request, 'Login efetuado Sucesso!')
        return redirect('usuario:index')
    messages.error(request, 'E-mail e/ou senha inválido!')
    return redirect('usuario:submit_login')

def user_logout(request):
    logout(request)
    return redirect('usuario:submit_login')

def index(request):
    return render(request, 'usuario/index.html')

def index_perfil(request):
    List = None

    nome = request.GET.get('profissao')
    cidade = request.GET.get('destino')

    if request.user is authenticate:
        if nome and cidade:

            List = Usuario.objects.filter((Q(cidade__contains=cidade))
                                          & (Q(perfil__nome__contains=nome))
                                          & (Q(perfil__isnull=False))
                                          )

        return render(request, 'usuario/index.html', {'List': List})
    elif nome:
        List = Usuario.objects.filter(perfil__nome__contains=nome)
    return render(request, 'usuario/home.html', {'List': List})


