from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [

    path(
        '',
        views.listar_latas,
        name='listar_latas'
    ),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ),  name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ),  name='logout'),

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
