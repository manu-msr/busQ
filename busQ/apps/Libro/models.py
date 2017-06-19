# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..Biblioteca.models import Biblioteca

# Create your models here.
class Libro(models.Model):
	titulo = models.CharField(max_length=50, null=False, blank=False)
	autor = models.CharField(max_length=100, null=False, blank=False)
	anio = models.PositiveSmallIntegerField(null=True, blank=True)
	bibliotecas = models.ManyToManyField(Biblioteca)
		