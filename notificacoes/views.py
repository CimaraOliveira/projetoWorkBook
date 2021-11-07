from django.shortcuts import render

def notificacoes(request):
    return render(request, 'notificacoes/notificacoes.html')