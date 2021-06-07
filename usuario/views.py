from django.shortcuts import render, redirect
from .models import Usuario, Perfil, Categoria
from django.contrib import messages


def login(request):
    return render(request, 'usuario/login.html')

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

        user = {'username': username, 'first_name': first_name, 'email': email, 'senha': senha, 'telefone': telefone,
                'perfil': request.POST['user']}

        user_db = Usuario.objects.filter(email=email)

        if not user_db:
            print('success')
            messages.success(request, 'Usuário Registrado com Sucesso!')

            new_user = Usuario.objects.create_superuser(username=username, first_name=first_name,
                                                        email=email, password=senha, cidade=cidade, telefone=telefone,
                                                        perfil=perfil)
            new_user.save()
            return redirect('usuario:cadastro')
        print('error')
        return __get__register(request, user, {'error': 'Usuário já Registrado. Tente outro e-mail!'})




