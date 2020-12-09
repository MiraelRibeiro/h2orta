from django.contrib import admin
from django.urls import path
from . import views

app_name = 'h2orta'

urlpatterns = [    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    path('criarconta/', views.criarConta, name='criar'),
    path('alterar/', views.alterar_senha, name='alterar'),
    path('deletar/', views.delete_user, name='deletar'),
    path('escolha/<int:id>', views.escolhaProduto, name='escolha'),
    path('comprar/<int:id>', views.comprar, name='comprar'),
    path('visualizacao/<int:id>', views.dadosFinais, name='visualizacao'),

]