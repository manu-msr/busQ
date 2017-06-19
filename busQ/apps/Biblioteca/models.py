# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Biblioteca(models.Model):
	nombre = models.CharField(max_length=50, null=False, blank=False)
	direccion = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.nombre
