from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Profissional, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .form import FormPerfil, FormDadosPessoais, FormEditProfissional
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from . import models
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator


app_name='usuario'

def home(request):
   profissional = Profissional.objects.all()
   context = {
       'profissional': profissional
   }
   return render(request, 'usuario/home.html',context)

def teste(request):
    return render(request, 'usuario/teste.html')

def index(request):
    return render(request, 'usuario/index.html')

def cadastro(request):
        if request.method != 'POST':
            return render(request, 'usuario/cadastro.html')

        username = request.POST['username']
        first_name = request.POST['first_name']
        telefone = request.POST['telefone']
        cidade = request.POST['cidade']
        rua = request.POST['rua']
        uf = request.POST['uf']
        bairro = request.POST['bairro']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not email or not username or not senha \
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

        new_user = Usuario.objects.create_superuser(username=username, first_name=first_name, telefone=telefone, email=email,password=senha,
                                                    cidade=cidade, rua=rua, uf=uf, bairro=bairro)
        new_user.save()
        return redirect('usuario:home')


@login_required(login_url='usuario:submit_login')
def add_perfil(request):
    form = FormPerfil(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.success(request, 'Perfil Profissional Adicionado com sucesso!')
        return redirect('usuario:add_perfil')
    else:
        form = FormPerfil(request.POST, request.FILES)
    context = {
        'form': form
    }
    return render(request, 'usuario/add_perfil.html',context)


def buscar(request):
   termo = request.GET.get('termo')

   if termo is None or not termo:
       messages.error(request, 'Campo não pode ser vazio!')
       return redirect('usuario:listarProfissional')

   campos = Concat('descricao',Value(' '),  'profissao')

   profissional = Profissional.objects.annotate(
        nome_profissao=campos
   ).filter(
        Q(profissao__icontains=termo) | Q(descricao__icontains=termo)

   )
   if not profissional:
       messages.error(request, 'Pesquisa não encontrada!')
       return redirect('usuario:listarProfissional')

   context = {
       'profissional': profissional
   }
   return render(request, 'usuario/buscar.html', context)



"""def categorias(request):
    categoria = Categoria.objects.all()

    context = {
        'categoria': categoria
    }
    return render(request, 'usuario/teste.html', context)"""

def submit_login(request):
    if request.method != 'POST':
        return render(request, 'usuario/submit_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, 'Login Efetuado Sucesso!')
        return redirect('usuario:listarProfissional')
    messages.error(request, 'E-mail e/ou senha inválido!')
    return redirect('usuario:submit_login')


"""class DetalhesProfissional(DetailView):
    model = models.Profissional
    template_name = 'usuario/detalhesProfissional.html'
    context_object_name = 'profissional'
    pk_id_url_kwarg = 'pk'"""

class DetalhesProfissional(DetailView):
    model = models.Profissional
    template_name = 'usuario/detalhesProfissional.html'
    context_object_name = 'profissional'
    slug_id_url_kwarg = 'slug'



"""def detalhesProfissional(request,id):
    usuario = Usuario.objects.get(id=id)
    profisssional = get_object_or_404(Profissional, user_id=usuario)

    context = {
        'profisssional':profisssional
    }

    return render(request, "usuario/detalhesProfissional.html",context)"""


def logout_user(request):
    request.session.flush()
    logout(request)
    return redirect('usuario:home')

def listarProfissional(request):
    profissional = Profissional.objects.all()
    paginator = Paginator(profissional, 2)
    page = request.GET.get('p')
    profissional = paginator.get_page(page)
    context = {
        'profissional':profissional
    }
    return render(request, 'usuario/listarProfissional.html',context)

def dadosPessoais(request, id):
    data = {}
    usuario = Usuario.objects.get(id=id)
    form = FormDadosPessoais(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('usuario:dadosPessoais', usuario.id)

    data['form'] = form
    data['usuario'] = usuario
    return render(request, 'usuario/dadosPessoais.html',data)


def dadosProfissional(request, user_id):
    data = {}
    profissional = Profissional.objects.get(user_id=user_id)

    form = FormEditProfissional(request.POST or None, instance=profissional)
    if form.is_valid():
        form.save()
        return redirect('usuario:dadosProfissional', profissional.user_id)
    data['form'] = form
    data['profissional'] = profissional
    return render(request, 'usuario/dadosProfissional.html', data)