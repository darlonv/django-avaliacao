from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def cadastrar(request):
    if request.method == "GET":
        # Caso requisição GET, é apresentada a pagina de cadastro
        # com o formulário a ser preenchido
        return render(request, "cadastrar.html")

    else:
        # Caso requisição POST, são processados os dados do formulario
        # já preenchido
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Verifica se esse usuário já existe
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Usuário já cadastrado")

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        return HttpResponse(username)


def logar(request):
    # Caso o usuário já esteja autenticado, redireciona para a página de avaliação
    if request.user.is_authenticated:
        return redirect(avaliacao)

    # caso seja um get, apresenta o formulário para logar
    if request.method == "GET":
        return render(request, "logar.html")
    # Caso seja uma requisição POST, entende que o formulário foi preenchido e
    # realiza a autenticação
    else:
        # obtém dados do formulário
        username = request.POST.get("username")
        password = request.POST.get("password")

        # verifica o login e senha do usuário
        user = authenticate(username=username, password=password)
        if user:
            # realiza a autenticação na sesssão
            login(request, user)
            # redireciona para a página de avaliação
            return redirect(avaliacao)
            # return HttpResponse("Usuário autenticado")
        else:
            return HttpResponse("Email ou senha inválidos")


# Página de logout
@login_required(login_url="/auth/login/")
def deslogar(request):
    # Atualiza a sessão
    logout(request)
    # redireciona para a página de login
    return render(request, "logar.html")


# Página com trabalhos a serem avaliados
@login_required(login_url="/auth/login/")
def avaliacao(request):
    return render(request, "avaliacao.html")


# Página de avaliação de trabalho
@login_required(login_url="/auth/login/")
def avaliar(request):
    return render(request, "avaliar.html")
