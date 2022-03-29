from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario,Profissional
from avaliacao.models import Avaliacao
from django.contrib.auth.decorators import login_required
from .form import AvaliacaoForm
from django.db.models import Avg
from django.core.paginator import Paginator
from django.contrib import messages


@login_required(login_url='usuario:submit_login')
def avaliacao(request,id):
    usuario = Usuario.objects.get(id=id)
    profissional = Profissional.objects.get(user=usuario)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        messages.success(request, 'Avaliação realizada com Sucesso!')
        return redirect('avaliacao:clientelistarAvaliacoes', id)
    else:
        form = AvaliacaoForm()
    context = {
        'form': form,
        'profissional': profissional
    }
    return render(request, 'avaliacao.html', context)

def listarAvaliacao(request):
    usuario = Usuario.objects.get(id=request.user.id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario).order_by('-id')
    paginator = Paginator(avaliacao, 3)
    page = request.GET.get('p')
    avaliacao = paginator.get_page(page)
    total_pessoas = Avaliacao.objects.filter(profissional_id=usuario).count()
    media = Avaliacao.objects.filter(profissional_id=usuario).aggregate(avg_rating=Avg('nota'))
    context = {
        'avaliacao': avaliacao,
        'total_pessoas': total_pessoas,
        'media':media
    }

    return render(request, 'listarAvaliacao.html', context)


def clientelistarAvaliacoes(request,id):
    usuario = Usuario.objects.get(id=id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario).order_by('-id')
    paginator = Paginator(avaliacao, 3)
    page = request.GET.get('p')
    avaliacao = paginator.get_page(page)
    total_pessoas = Avaliacao.objects.filter(profissional_id=usuario).count()
    media = Avaliacao.objects.filter(profissional_id=usuario).aggregate(avg_rating=Avg('nota'))
    context = {
        'avaliacao':avaliacao,
        'total_pessoas': total_pessoas,
        'media': media

    }
    return render(request, 'clientelistarAvaliacoes.html', context)

