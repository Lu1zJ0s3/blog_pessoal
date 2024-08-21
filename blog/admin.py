from django.contrib import admin
from .models import Curso, Interesse

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome',)
