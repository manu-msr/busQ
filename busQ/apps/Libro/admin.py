# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..Libro.models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	pass