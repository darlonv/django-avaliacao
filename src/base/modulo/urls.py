from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("login/", views.logar, name="logar"),
    path("logout/", views.deslogar, name="deslogar"),
    path("avaliacao/", views.page_avaliacao, name="avaliacao"),
    path("avaliar/", views.page_avaliar, name="avaliar"),
    path("ok/", views.page_ok, name="ok"),
    path("error/", views.page_error, name="error"),
    path("processa_avaliacao/", views.processa_avaliacao, name="processa_avaliacao"),
]
