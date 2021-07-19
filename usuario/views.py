from django.shortcuts import render, redirect
from .models import Usuario, Profissional, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .form import FormPerfil
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator


app_name='usuario'

def home(request):
   perfil = Profissional.objects.all()

   context = {
       'perfil': perfil
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

        new_user = Usuario.objects.create_superuser(username=username, telefone=telefone, email=email,password=senha,
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

   campos = Concat('profissao',Value(' '), 'cidade')

   perfil = Usuario.objects.annotate(
        nome_profissao=campos
   ).filter(
        Q(nome_profissao__icontains=termo) | Q(cidade__icontains=termo)

   )
   if not perfil:
       messages.error(request, 'Pesquisa não encontrada!')
       return redirect('usuario:listarProfissional')

   context = {
       'perfil': perfil
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

class DetalhesProfissional(DetailView,LoginRequiredMixin):
    model = models.Profissional
    template_name = 'usuario/detalhesProfissional.html'
    context_object_name = 'perfil'
    slug_id_url_kwarg = 'slug'


def logout_user(request):
    request.session.flush()
    logout(request)
    return redirect('usuario:home')

def listarProfissional(request):
    perfil = Profissional.objects.all()
    paginator = Paginator(perfil, 2)
    page = request.GET.get('p')
    perfil = paginator.get_page(page)
    context = {
        'perfil':perfil
    }
    return render(request, 'usuario/listarProfissional.html',context)


