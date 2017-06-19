# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..Biblioteca.models import Biblioteca

# Register your models here.
@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion')
	list_filter = ('nombre',)
	search_fields = ('nombre',)
