# Renderização de páginas
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Manipulação de usuários
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from aval.models import Trabalho, Avaliacao

# Formulários
from .forms import AvaliacaoForm


# Create your views here.
def page_signin(request):
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
            username=username, email=email, password=password, is_staff=False
        )
        user.save()
        return HttpResponse(username)


def page_login(request):
    context = dict()
    # Caso o usuário já esteja autenticado, redireciona para a página de avaliação
    if request.user.is_authenticated:
        return redirect(page_avaliacao)

    # caso seja um get, apresenta o formulário para logar
    if request.method == "GET":
        # Obtém a página a ser carregada após login, caso esteja definida
        next_page = request.GET.get("next", "")
        context["next"] = next_page

        return render(request, "logar.html", context)
    # Caso seja uma requisição POST, entende que o formulário foi preenchido e
    # realiza a autenticação
    else:
        # obtém dados do formulário
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next", None)

        # verifica o login e senha do usuário
        user = authenticate(username=username, password=password)
        if user:
            # realiza a autenticação na sesssão
            login(request, user)
            if next_page:
                # return HttpResponse(f"Usuário autenticado - {next_page}")
                # redireciona para a página de avaliação

                return redirect(next_page)
            else:
                # redireciona para a próxima página definida
                return redirect(page_avaliacao)
                # return HttpResponse(f"Usuário autenticado - {next_page}")

        else:
            return HttpResponse("Email ou senha inválidos")


# Página de logout
@login_required(login_url="/auth/login/")
def page_logout(request):
    if request.method == "GET":
        # redireciona para a página de login
        return render(request, "logout.html")
    else:
        # processa o logout
        # Atualiza a sessão
        logout(request)
        # redireciona para a página de login
        return render(request, "logar.html")


# Página com trabalhos a serem avaliados
@login_required(login_url="/auth/login/")
def page_avaliacao(request):
    context = dict()
    # obtém os trabalhos a serem avaliados
    trabalhos_pendentes = Avaliacao.objects.filter(
        avaliador=request.user, status="P"
    )  # trabalhos pendentes
    context["pendentes"] = list(trabalhos_pendentes)
    context["n_trabalhos_pendentes"] = len(trabalhos_pendentes)

    trabalhos_avaliados = Avaliacao.objects.filter(
        avaliador=request.user, status="A"
    )  # trabalhos avaliados
    context["avaliados"] = trabalhos_avaliados
    context["n_trabalhos"] = len(trabalhos_pendentes) + len(trabalhos_avaliados)

    # obtém os trabalhos já avaliados
    return render(request, "avaliacao.html", context)


# Página de avaliação de trabalho
@login_required(login_url="/auth/login/")
def page_avaliar(request):
    context = dict()

    # Verififica se é um GET ou POST
    # GET renderiza a página para avaliar. POST processa um formulário recebido
    if request.method == "GET":
        # obtém o id do trabalho
        tid = request.GET.get(
            "tid", None
        )  # None será o valor padrão, caso o tid não seja passado
        # objeto do usuário no BD
        user = request.user

        context["tid"] = tid

        # obtém o trabalho
        trabalho = Trabalho.objects.filter(identificador=tid).first()
        if not trabalho:
            # redireciona para a página de trabalho invalido
            context["error_message"] = f"Trabalho inválido. tid = {tid}"
            return render(request, "error.html", context)

        # verifica se o avaliador está associado ao trabalho
        aval = Avaliacao.objects.filter(trabalho=trabalho, avaliador=user).first()
        if not aval:
            # redireciona para a página de avaliador não associado
            context["error_message"] = "Avaliador não associado ao trabalho"
            return render(request, "error.html", context)

        form = AvaliacaoForm()  # Cria o formulário de avaliação

        context["form"] = form  # Passa o formulário para a página
        context["avaliador"] = user.username
        context["titulo"] = trabalho.titulo
        context["autores"] = trabalho.autores
        return render(request, "avaliar.html", context)  # renderiza a página
    else:
        # Processa os dados recebidos via formulário
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            tid = request.POST.get("tid")

            # obtem dados do trabalho e do avaliador
            trabalho = Trabalho.objects.get(identificador=tid)
            avaliador = request.user

            # obtém o registro da avaliacao no BD
            avaliacao = Avaliacao.objects.get(trabalho=trabalho, avaliador=avaliador)

            # atualiza os dados do registro
            avaliacao.nota_diagramacao = form.data["diagramacao"]
            avaliacao.nota_texto = form.data["texto"]
            avaliacao.nota_apresentacao = form.data["apresentacao"]
            avaliacao.status = "A"  # Marca como avaliado

            # Salva os dados da avaliacao no BD
            avaliacao.save()

            # Redireciona para a página de ok
            # context["ok_message"] = "Trabalho avaliado. Obrigado."
            # return render(request, "ok.html", context)
            # Redireciona para a página com a lista de trabalhos
            return redirect(page_avaliacao)
        else:
            context["error_message"] = "Erro ao processar os dados preenchidos"
            return render(request, "error.html", context)


# Página de mensagens
@login_required(login_url="/auth/login/")
def page_ok(request):
    context = {"ok_message": "Página de ok."}
    return render(request, "ok.html", context)


# Página de mensagem de erro
@login_required(login_url="/auth/login/")
def page_error(request):
    context = dict()
    context["error_message"] = "Mensagem de erro."
    return render(request, "error.html", context)


# Página de status dos trabalhos
@login_required(login_url="/auth/login/")
def page_status_trabalhos(request):
    context = dict()
    trabalhos = dict()
    titulos = []
    if request.user.is_staff:
        # obtém os trabalhos
        trabalhos_query = Trabalho.objects.all()
        # Verifica o número de avaliadores
        # Avaliadores
        # Já avaliados

        print("---")
        for trab in trabalhos_query:
            trabalhos[trab.identificador] = {
                "tid": trab.identificador,
                "titulo": trab.titulo,
            }
            titulos.append(trab.titulo)
        print("+++")

        # return HttpResponse(trabalhos)
        context["trabalhos"] = trabalhos
        context["titulos"] = titulos
        return render(request, "status_trabalhos.html", context)

    context["error_message"] = "Sem permissão"
    return render(request, "error.html", context)


# Página de testes
@login_required(login_url="/auth/login/")
def page_teste(request):
    context = dict()
    return render(request, "teste.html", context)
