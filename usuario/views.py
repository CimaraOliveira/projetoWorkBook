from django.shortcuts import render, redirect
from .models import Usuario

def login(request):
    return render(request, 'usuario/login.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'usuario/cadastro.html')

    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    cidade = request.POST['cidade']
    estado = request.POST['estado']
    telefone = request.POST['telefone']

    new_user = Usuario.objects.create_superuser(username=username, first_name=first_name, last_name=last_name,
                                                email=email, cidade=cidade, estado=estado, telefone=telefone, password=password)
    new_user.save()
    new_user.save()
    return redirect('usuario:cadastro')
