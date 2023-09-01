from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("login/", views.logar, name="logar"),
    path("logout/", views.deslogar, name="deslogar"),
    path("avaliacao/", views.avaliacao, name="avaliacao"),
    path("avaliar/", views.avaliar, name="avaliar"),
]
