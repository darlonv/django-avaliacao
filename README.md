# django-avaliacao
Sistema para avaliação de posteres em eventos científicos, utilizando o framework Django.

Versão com objetivo de aprendizagem do Django.


Para executar:

1. clonar o projeto 
    ```bash
    git clone
    ```
1. criar e ativar ambiente virtual
    ```bash
    #criar ambiente virtual
    python3 -m venv venv #linux
    #ativar ambiente virtual
    source env/bin/activate #linux
    source env/Scripts/Activate.bat #cmd
    source env/Scripts/Activate.ps1 #powershell
    ```
1. instalar as bibliotecas
    ```bash
    pip3 install -r requirements.txt
    ```
1. executar o servidor do Django
    ```bash
    cd django-avalicacao/src/base
    python3 manage.py runserver
    ```