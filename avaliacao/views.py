from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario,Profissional
from avaliacao.models import Avaliacao
from django.contrib.auth.decorators import login_required
from .form import AvaliacaoForm

@login_required(login_url='usuario:submit_login')
def avaliacao(request,id):
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
        return redirect('usuario:listarProfissional')
    else:
        form = AvaliacaoForm()
    context = {
        'form': form,
        'profissional': profissional
    }
    return render(request, 'avaliacao.html', context)

def listarAvaliacao(request):
    usuario = Usuario.objects.get(id=request.user.id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario)

    context = {
        'avaliacao': avaliacao
    }

    return render(request, 'listarAvaliacao.html', context)


def clientelistarAvaliacoes(request,id):
    usuario = Usuario.objects.get(id=id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario)

    context = {
        'avaliacao':avaliacao
    }
    return render(request, 'clientelistarAvaliacoes.html', context)

