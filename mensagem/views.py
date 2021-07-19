from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensagem
from usuario.models import Usuario,Profissional
from .forms import MensagemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

app_name = 'mensagem'

def teste(request):
    return render(request, 'teste.html')

@login_required(login_url='usuario:submit_login')
def enviarMensagem(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    perfil = get_object_or_404(Perfil, user_id=usuario)
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


def mensagens_por_usuario(request):
    # essa query vai pegar a ultima mensagem feita pelo remetente ou pelo destinatario.

    sql = "select * from usuario u where u.id in (select u2.id from usuario u2" \
          "	inner join Mensagen m on(u2.id = m.remetente_id) " \
          "	where u2.id != (select u3.id from usuario u3 where u3.id = %s and u3.id =" \
          " m.destinatario_id) ORDER by m.id desc)" \
          "	OR u.id in (" \
          "	select u4.id from usuario u4 " \
          "inner join Mensagen m2 on(u4.id = m2.destinatario_id)" \
          "	where u4.id != (select u5.id from usuario u5 where u5.id =" \
          " %s and u5.id = m2.remetente_id) ORDER by m2.id DESC) ORDER by u.id DESC"
    usuarios = Usuario.objects.raw(sql, [request.user.id, request.user.id])

    mensagens = []
    id = request.user.id
    for user in usuarios:
        if user.id != request.user.id:
            mensagem = Mensagem.objects.filter((Q(destinatario__id=user.id) & Q(remetente__id=id)) | (Q(remetente__id=user.id) & Q(destinatario__id=id))).last()
            if mensagem:
                mensagens.append(mensagem)

    return mensagens


@login_required(login_url='usuario:submit_login')
def listarMensagem(request, idDestinatario):
    user = request.user.id
    mensagens = mensagens_por_usuario(request)
    context = {
        'mensagens': mensagens,
        'remetente': Usuario.objects.get(id=user),
        'destinatario': Usuario.objects.get(id=idDestinatario)
    }
    return render(request, 'listarMensagem.html', context)


@login_required(login_url='usuario:submit_login')
def detalheMensagem(request, idRemetente, idDestinatario):
    #print(idRemetente, idDestinatario)
    mensagens = mensagens_por_usuario(request)
    mensagens_detalhe = Mensagem.objects.filter(
        (Q(destinatario__id=idDestinatario) & Q(remetente__id=idRemetente)) |
        (Q(destinatario__id=idRemetente) & Q(remetente__id=idDestinatario))).order_by('id')

    #for m in mensagens_detalhe:
     #   print(m.texto)

    context = {
        'mensagens_detalhe': mensagens_detalhe,
        'mensagens': mensagens,
        'remetente': Usuario.objects.get(id=idRemetente),
        'destinatario': Usuario.objects.get(id=idDestinatario)
    }
    return render(request, 'listarMensagem.html', context)


@login_required(login_url='usuario:submit_login')
def responderMensagem(request, idRemetente, idDestinatario):
    respMensagem = Mensagem.objects.filter(Q(remetente__id=idRemetente) & Q(destinatario__id=idDestinatario)).first()
    user = request.user.id
    form = MensagemForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('listarMensagem', idDestinatario=idDestinatario)
    else:
        form = MensagemForm(request.POST)
        print(form)
    context = {
        'form': form,
        'respMensagem': respMensagem,
        'remetente': user
    }
    return render(request, 'responderMensagem.html', context)



