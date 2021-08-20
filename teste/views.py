from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from .form import AvaliacaoForm
from usuario.models import Usuario, Profissional
from django.contrib.auth.decorators import login_required
from .models import TesteAvaliacao
from django.contrib.admin.filters import SimpleListFilter
app_name = 'teste'

"""
    select * from  usuario_profissional as prof inner join usuario 
    as usu on (prof.user_id=usu.id) where  prof.user_id=2

    """


"""
print ('**', profissional)
    print('***usuario logado', user)
    print('**id profissional', profissional.user.id)
"""

@login_required(login_url='usuario:submit_login')
def avaliacao_teste(request,id):

    """sql = select * from  usuario_profissional as prof inner join usuario
    as usu on (prof.user_id=usu.id) where  prof.user_id= usu.id"""
    """usuario = get_object_or_404(Usuario, id=id)
    profissional = get_object_or_404(Profissional, user_id=usuario)
    user = request.user.id"""
    form = AvaliacaoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('teste/avaliacao_teste.html')
    else:
        form = AvaliacaoForm(request.POST)

    context = {
        'form': form,
        'profissional': profissional,
        #'usuario': usuario
    }
    return render(request,'teste/avaliacao_teste.html', context)







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

