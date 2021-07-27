from django.shortcuts import render, redirect, get_object_or_404
from .models import Avaliacao
from usuario.models import Usuario,Profissional
from datetime import datetime
from django.contrib.auth.decorators import login_required

def teste(request):
    return render(request, 'teste.html')

def _request_user(request):
    try:
        usuario = get_object_or_404(Usuario, id=request.user)
        perfil = get_object_or_404(Profissional, user_id=usuario)


        if perfil:
            return perfil
    except Exception as err:
        print(err)
    return None

def _request_perfil(id):
    try:
        usuario = get_object_or_404(Usuario, id=id)
        prof = get_object_or_404(Profissional, user_id=usuario)
        if prof.perfil:
            return prof
    except Exception as err:
        print(err)
    return None

def avaliacao(request, id):
    return render(request, 'avaliacao.html', {'perfil': _request_perfil(id)})


def avaliar(request, id):

    if request.POST['descricao']:
       client = _request_user(request)
       prof = _request_perfil(id)
       descricao = request.POST['descricao']
       nota = request.POST['fb']

       data_e_hora_atuais = datetime.now()
       data = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
       if client and prof:
            avaliar = Avaliacao.objects.create(descricao=descricao, nota=nota, cliente=client, profissional=prof, data_avaliacao=data)
            avaliar.save()

       return redirect('usuario:home')
    return avaliacao(request)

@login_required(login_url='usuario:submit_login')
def listAvaliacao(request):
    avaliar = Avaliacao.objects.filter(profissional=request.user.id)

    return render(request, 'ListAvaliacao.html', {'avaliar': avaliar})

