# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Requisicao

class AdminRequisicao(admin.ModelAdmin):
	list_display = ('palavra', 'quantidade', 'url', 'data', 'arquivo')

admin.site.register(Requisicao, AdminRequisicao)