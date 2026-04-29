from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.listar_latas,
        name='listar_latas'
    ),

    path(
        'adicionar/',
        views.adicionar_lata,
        name='adicionar_lata'
    ),

    path(
        'editar/<int:id>/',
        views.editar_lata,
        name='editar_lata'
    ),

    path(
        'apagar/<int:id>/',
        views.apagar_lata,
        name='apagar_lata'
    ),
]
