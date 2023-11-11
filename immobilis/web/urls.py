from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginpost/', views.login_post, name='loginpost'),
    path('logout/', views.logout, name='logout'),
    path('busca/', views.busca, name='busca'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('perfis/', views.perfis, name='perfis'),
    path('telas/', views.telas, name='telas'),
    path('imoveis/', views.imoveis, name='imoveis'),
    path('tiposimoveis/', views.tiposimoveis, name='tiposimoveis'),
    path('detalhesimovel/', views.detalhesimovel, name='detalhesimovel'),
]