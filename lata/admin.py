from django.contrib import admin
from .models import Marca, Tamanho, Lata


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id_marca', 'nome_marca', 'descricao')
    search_fields = ('nome_marca',)


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('id_tamanho', 'tamanho')
    search_fields = ('tamanho',)


@admin.register(Lata)
class LataAdmin(admin.ModelAdmin):
    list_display = (
        'id_lata',
        'nome',
        'marca',
        'tamanho',
        'disponivel_portugal',
        'descontinuada',
    )
    list_filter = (
        'marca',
        'tamanho',
        'disponivel_portugal',
        'descontinuada',
    )
    search_fields = (
        'nome',
        'marca__nome_marca',
    )

# Register your models here.
