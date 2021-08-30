from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from .form import AvaliacaoForm
from usuario.models import Usuario, Profissional
from django.contrib.auth.decorators import login_required
from .models import TesteAvaliacao
from django.contrib.admin.filters import SimpleListFilter
app_name = 'teste'

"""usuario = get_object_or_404(Usuario, id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario)"""

@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,id):
    usuario = Usuario.objects.get(id=id)
    profissional = Profissional.objects.get(user=usuario)
    print("usuario", usuario)
    print("Profissional", profissional)
    if request.method == 'POST':
         form = AvaliacaoForm(request.POST)
         if form.is_valid():
             obj = form.save(commit=False)
             obj.user = request.user
             obj.save()
             #obj.save()
         return redirect('listar')
    else:
        form = AvaliacaoForm()
    context = {
        'form': form,
        'profissional':profissional
    }
    return render(request,'teste/avaliacao_teste.html', context)


"""
def enviarMensagem(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    perfil = get_object_or_404(Profissional, user_id=usuario)
    user = request.user.id
    form = MensagemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listarMensagem')
    else:
        form = MensagemForm(request.POST)

    context = {
        'form': form,
        'perfil': perfil,
        'remetente': user
    }
    return render(request, 'enviarMensagem.html', context)
"""

"""
usuario = get_object_or_404(Usuario, id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario)
"""

"""@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,id):
    usuario = Usuario.objects.get(id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario)
    #profissional = Profissional.objects.get(user_id=usuario)
    print("usuaruio profissional", usuario)
    print("profissional", profissional)
    user = request.user.id
    if request.method == 'POST':
         form = AvaliacaoForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect('listar')
    else:
        form = AvaliacaoForm()

    context = {
        'form': form,
        'profissional': profissional,
        #'cliente': user,
        'cliente':user
    }
    return render(request,'teste/avaliacao_teste.html', context)"""



"""
    select * from  usuario_profissional as prof inner join usuario 
    as usu on (prof.user_id=usu.id) where  prof.user_id=2

    """
"""
print ('**', profissional)
    print('***usuario logado', user)
    print('**id profissional', profissional.user.id)
"""



"""

@login_required(login_url='usuario:submit_login')
def listar(request):
    usuario = Usuario.objects.get(id=request.user.id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario)

    context = {
        'avaliacao':avaliacao
    }
    return render(request, 'listar.html', context)
"""

def listar(request):
    usuario = Usuario.objects.get(id=request.user.id)
    listar = TesteAvaliacao.objects.filter(profissional_id=usuario)

    context = {
        'listar': listar
    }

    return render(request, 'teste/listar.html', context)

"""sql = select * from  usuario_profissional as prof inner join usuario
    as usu on (prof.user_id=usu.id) where  prof.user_id= usu.id"""


""" FUNCIONANDO
@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,id):
    usuario = get_object_or_404(Usuario, id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario)
    if request.method == 'POST':
         form = AvaliacaoForm(request.POST)
         if form.is_valid():
             obj = form.save(commit=False)
             obj.save()
             form.save()
         return redirect('listar')
    else:
        form = AvaliacaoForm()

    context = {
        'form': form,
        'profissional':profissional
    }
    return render(request,'teste/avaliacao_teste.html', context)
"""