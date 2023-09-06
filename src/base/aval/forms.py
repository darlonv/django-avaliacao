from django import forms
from .models import Avaliacao


# class CadastrarForm(forms.Form):
#     nome = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     senha = password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class AvaliacaoForm(forms.Form):
    diagramacao = forms.IntegerField(min_value=0, max_value=10, initial=0)
    texto = forms.IntegerField(min_value=0, max_value=10, initial=0)
    apresentacao = forms.IntegerField(min_value=0, max_value=10, initial=0)
