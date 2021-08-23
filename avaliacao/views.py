from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario,Profissional
from avaliacao.models import Avaliacao
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# funcao que retorna o usuario logado
def _request_user(request):
    try:
        user = Usuario.objects.get(id=request.user.id)
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
       prof = Profissional.objects.get(user_id=user_id)

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

       """if not nota:
           messages.error(request, 'Deixe sua estrela para o profissional!')"""
           #return render(request, 'avaliacao.html', {'profissional': _request_profissional(user_id)})

       if client and prof:
            avaliar = Avaliacao.objects.create(descricao=descricao, nota=nota, cliente=client, profissional=prof, data_avaliacao=data)
            avaliar.save()



       return redirect('usuario:listarProfissional')

    return avaliacao(request)

def get_avaliacao(id):
    sql_prof = "select * from usuario u " \
               "inner join usuario_profissional up on u.id = up.user_id " \
               "where u.id = %s"

    prof = Usuario.objects.raw(sql_prof, [id])

    if prof:
        sql = "select * " \
        "from avaliacao a where " \
        "a.id in (select a2.id from avaliacao a2 " \
        "inner join usuario_profissional p on p.id = a2.profissional_id " \
        "inner join usuario u on u.id = p.user_id where u.id = %s)"
        return Avaliacao.objects.raw(sql, [id])

    sql_user = "select * from avaliacao a where a.id " \
               "in (select a2.id from avaliacao a2 " \
               "inner join usuario u on u.id = a2.cliente_id " \
               "where u.id = %s)"
    return Avaliacao.objects.raw(sql_user, [id])

@login_required(login_url='usuario:submit_login')
def listAvaliacao(request):
    id = request.user.id
    # select *
    # from avaliacao a
    # where
    # a.id in (
    #     select a2.id from avaliacao a2
    # inner join usuario u on u.id = a2.cliente_id
    # where u.id = 3
    # )

    # select *
    # from avaliacao a
    # where
    # a.id in (
    #     select a2.id from avaliacao a2
    # inner join usuario_profissional p on p.id = a2.profissional_id
    # inner join usuario u on u.id = p.user_id
    # where u.id = 2
    # )
    #avaliar = Avaliacao.objects.filter(profissional=request.user.id)

    return render(request, 'ListAvaliacao.html', {'avaliar': get_avaliacao(id)})


def avaliacoesProfissional(request):
    pass

