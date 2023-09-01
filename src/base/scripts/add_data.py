# from base.models import Trabalho
from modulo.models import Trabalho, Avaliacao
from django.contrib.auth.models import User

import json

USERS_FILE = "users.json"


def run():
    print("Running script")

    ##adicionando usuários
    with open(USERS_FILE) as file:
        users = json.load(file)
        print(users)
