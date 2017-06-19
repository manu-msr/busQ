# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.list import ListView
from ..Biblioteca.models import Biblioteca

# Create your views here.
class ListViewBiblioteca(ListView):
	model = Biblioteca
	template_name = 'listaBibliotecas.html'
	context_object_name = 'bibliotecas'
