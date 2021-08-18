from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from .form import AvaliacaoForm
from usuario.models import Usuario, Profissional
from django.contrib.auth.decorators import login_required
from .models import TesteAvaliacao

app_name = 'teste'

"""
    select * from  usuario_profissional as prof inner join usuario 
    as usu on (prof.user_id=usu.id) where  prof.user_id=2

    """

@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,user_id):
    descricao = request.POST.get('descricao')
    nota = request.POST.get('nota')
    data_avaliacao = request.POST.get('data_avaliacao')

    #usuario = Usuario.objects.get(pk=id)
    profissional = Profissional.objects.get(prof_id=user_id)


    #profissional = get_object_or_404(Profissional, user_id=usuario.id)
    #profissional = Profissional.objects.get(user_id=usuario.id)

    salvar = TesteAvaliacao.objects.create(descricao=descricao, nota=nota,
                                           data_avaliacao=data_avaliacao,
                                           profissional=profissional
                                           )
    salvar.save()
    return render(request, 'teste/avaliacao_teste.html')

"""@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,user_id):
    descricao = request.POST.get('descricao')
    nota = request.POST.get('nota')
    data_avaliacao = request.POST.get('data_avaliacao')"""


"""@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,id):
    usuario = get_object_or_404(Usuario, id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario.id)
    user = request.user.id

    print ('**', profissional)
    print('***usuario logado', user)

    form = AvaliacaoForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('usuario:listarProfissional')
    else:
        form = AvaliacaoForm(request.POST)

    context = {
        'form': form,
        'profissional': profissional,
        'usuario': usuario
    }
    return render(request,'teste/avaliacao_teste.html', context)"""







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
    listar = TesteAvaliacao.objects.filter(profissional=usuario.id)

    context = {
        'listar': listar
    }

    return render(request, 'teste/listar.html', context)

