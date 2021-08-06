from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario,Profissional
from avaliacao.models import Avaliacao
from datetime import datetime
from .form import AvaliacaoForm
from django.contrib.auth.decorators import login_required

# funcao que retorna o usuario logado
def _request_user(request):
    try:
        user = Usuario.objects.get(id=request.user.id)
        if user:
            return user
    except Exception as err:
        print(err)
    return None

# funcao que retorna o perfil pelo id
def _request_perfil(id):
    try:
       usuario = get_object_or_404(Usuario, id=id)
       prof = Profissional.objects.get(user_id=usuario)
       #prof = get_object_or_404(Profissional, user_id=usuario)
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

       return redirect('usuario:listarProfissional')
    return avaliacao(request)

@login_required(login_url='usuario:submit_login')
def listAvaliacao(request):
    avaliar = Avaliacao.objects.filter(profissional=request.user.id)

    return render(request, 'ListAvaliacao.html', {'avaliar': avaliar})

