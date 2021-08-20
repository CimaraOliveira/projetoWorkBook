from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario,Profissional
from avaliacao.models import Avaliacao
from datetime import datetime
from django.contrib.auth.decorators import login_required

# funcao que retorna o usuario logado
def _request_user(request):
    try:
        user = Usuario.objects.get(id=request.user.id)
        print('*** usuarioLogado ******', user)
        if user:
            return user
    except Exception as err:
        print(err)
    return None

"""
select * from  usuario_profissional as prof inner join usuario as usu on (prof.user_id=usu.id) 
where  prof.user_id=2

"""

# funcao que retorna o perfil pelo id
def _request_profissional(user_id):
    try:
       #user =  Usuario.objects.get(id=id)
       prof = Profissional.objects.get(user_id=user_id)

       #print('**usuario profissional',user)
       print('**profissional', prof)


       if prof:
         return prof
    except Exception as err:
        print('error request_perfil',err)
    return None

def avaliacao(request, user_id):
    return render(request, 'avaliacao.html', {'profissional': _request_profissional(user_id)})


def avaliar(request, user_id):

    if request.POST['descricao']:
       client = _request_user(request)
       prof = _request_profissional(user_id)
       descricao = request.POST['descricao']
       nota = request.POST['fb']
       print("cliente",client, "profissional", prof)
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


@login_required(login_url='usuario:submit_login')
def listar(request):
    usuario = Usuario.objects.get(id=request.user.id)
    avaliacao = Avaliacao.objects.filter(profissional_id=usuario)

    context = {
        'avaliacao':avaliacao
    }
    return render(request, 'listar.html')
