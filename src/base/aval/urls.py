# urls do app aval
from django.urls import path
from . import views

urlpatterns = [
    ####
    # rotas principal. redireciona para a pagina com a lista de trabalhos
    ####
    path("", views.page_login),  # home
    ####
    # rotas para autenticação
    ####
    path("auth/singnin/", views.page_signin, name="signin"),  # cadastro
    path("auth/login/", views.page_login, name="login"),  # login
    path("auth/logout/", views.page_logout, name="logout"),  # logout
    ####
    # rotas para avaliação
    ####
    path("avaliacao/", views.page_avaliacao, name="avaliacao"),
    path("avaliar/", views.page_avaliar, name="avaliar"),
    ####
    # rotas para status (apenas staff)
    ####
    path("status/trabalhos/", views.page_status_trabalhos, name="status_trabalhos"),
    ####
    # rotas para mensagens
    ####
    path("ok/", views.page_ok, name="ok"),
    path("error/", views.page_error, name="error"),
    ####
    # teste
    ####
    path("teste/", views.page_teste, name="teste"),
]
