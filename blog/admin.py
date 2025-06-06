from django.contrib import admin
from .models import Curso, Interesse, Sobre

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('titulo',)