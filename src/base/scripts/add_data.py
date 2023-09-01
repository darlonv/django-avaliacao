# from base.models import Trabalho
from modulo.models import Trabalho, Avaliacao
from django.contrib.auth.models import User

import json

USERS_FILE = "scripts/users.json"
TRABALHOS_FILE = "scripts/trabalhos.json"
AVALIACOES_FILE = "scripts/avaliacoes.json"


def run():
    print("Running script")

    ##adicionando usuários
    print("== Adicionando usuários ==")
    with open(USERS_FILE, "r") as file:
        users = json.load(file)
        for username in users:
            print(f"Adicionando usuário {username}...", end=" ")

            # Verifica se esse usuário já existe
            user = User.objects.filter(username=username).first()
            if user:
                print("usuário já cadastrado.")
            else:
                email = users[username]["email"]
                password = users[username]["password"]
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                print(f"feito.")
