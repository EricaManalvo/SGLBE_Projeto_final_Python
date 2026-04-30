from django.urls import path
from .import views

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
    
    path(
        'exportar/excel/', 
        views.exportar_excel,
        name='exportar_excel'
        ),
    
    path(
        'exportar/pdf/', 
        views.exportar_pdf, 
        name='exportar_pdf'
        ),
]
