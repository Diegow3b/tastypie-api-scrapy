#-*- coding: utf-8 -*-

# Arquivo fabfile.py
from datetime import datetime
# aqui importando uns caras legais da api do fabric
# local - roda um comando de shell na máquina local
# run - roda um comando de shell no servidor remoto
# put - faz uma cópia via ssh (scp) pro servidor remoto
# env - configurações do ambiente
from fabric.api import local
from os.path import exists

import sys

def migrations():
    local("./manage.py makemigrations")
    local("./manage.py migrate")

def runserver():
    local("./manage.py runserver")

def rm_sqlite():
    local("rm project/db.sqlite3")

def shell():
    local("./manage.py shell")
