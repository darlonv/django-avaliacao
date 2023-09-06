# from base.models import Trabalho
from aval.models import Trabalho, Avaliacao
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
                staff = False
                if "is_staff" in users[username]:
                    staff = users[username]["is_staff"]

                user = User.objects.create_user(
                    username=username, email=email, password=password, is_staff=staff
                )
                user.save()
                print(f"feito.")

    ##adicionando trabalhos
    print("== Adicionando trabalhos ==")
    with open(TRABALHOS_FILE, "r") as file:
        trabalhos = json.load(file)
        for tid in trabalhos:
            print(f"Adicionando trabalho {tid}...", end=" ")

            # Verifica se esse usuário já existe
            trabalho = Trabalho.objects.filter(identificador=tid).first()

            if trabalho:
                print("Trabalho já cadastrado.")
            else:
                trabalho = Trabalho()
                trabalho.identificador = tid

                if "titulo" in trabalhos[tid]:
                    trabalho.titulo = trabalhos[tid]["titulo"]

                if "autores" in trabalhos[tid]:
                    trabalho.autores = trabalhos[tid][
                        "autores"
                    ]  # toda a lista é adicionada
                else:
                    trabalho.autores = []

                # verifica se a categoria está incluída
                if "categoria" in trabalhos[tid]:
                    trabalho.categoria = trabalhos[tid]["categoria"]
                trabalho.save()
                print(f"feito.")

    ##adicionando trabalhos
    print("== Associando avaliadores aos trabalhos ==")
    with open(AVALIACOES_FILE, "r") as file:
        avaliacoes = json.load(file)
        for tid in avaliacoes:
            print(f"Associando avaliadores ao trabalho {tid}...")

            # Verifica se o trabalho já foi cadastrado
            trabalho = Trabalho.objects.filter(identificador=tid).first()
            if not trabalho:
                print(f"Trabalho com id {tid} não cadastrado no sistema.")

            print(f"\tAutores do trabalho: {trabalho.autores}")
            print(f"\tAvaliadores: {avaliacoes[tid]['avaliadores']}")

            for avaliador_trabalho in avaliacoes[tid]["avaliadores"]:
                # verifica se o avaliador já foi cadastrado
                avaliador = User.objects.filter(username=avaliador_trabalho).first()
                if not avaliador:
                    print(
                        f"\tAvaliador {avaliador_trabalho} não cadastrado no sistema."
                    )

                # verifica se o avaliador já está associado ao trabalho
                avaliacao = Avaliacao.objects.filter(
                    trabalho=trabalho, avaliador=avaliador
                ).first()

                if avaliacao:
                    print(f"\t{avaliador_trabalho} já é avaliador do trabalho {tid}")
                else:
                    avaliacao = Avaliacao()
                    avaliacao.trabalho = trabalho
                    avaliacao.avaliador = avaliador
                    avaliacao.save()

            print(f"\tfeito.")
