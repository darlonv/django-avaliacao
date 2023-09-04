from django.urls import path
from . import views

urlpatterns = [
    path("singnin/", views.page_signin, name="signin"),
    path("login/", views.page_login, name="login"),
    path("logout/", views.page_logout, name="logout"),
    path("processa_logout/", views.processa_logout, name="processa_logout"),
    path("avaliacao/", views.page_avaliacao, name="avaliacao"),
    path("avaliar/", views.page_avaliar, name="avaliar"),
    path("ok/", views.page_ok, name="ok"),
    path("error/", views.page_error, name="error"),
    path("processa_avaliacao/", views.processa_avaliacao, name="processa_avaliacao"),
    path("teste/", views.page_teste, name="teste"),
]
