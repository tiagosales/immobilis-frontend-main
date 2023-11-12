from django.shortcuts import render
from .utils import is_user_logged_in, login_post, logout
from django.http import JsonResponse
import requests


def login(request):
    return render(request, 'login.html')

def busca(request):
    return render(request, 'busca.html')

def usuarios(request):
    return render(request, 'admin_usuarios.html')

def perfis(request):
    return render(request, 'admin_perfis.html')

def telas(request):
    return render(request, 'admin_telas.html')

def imoveis(request):
    return render(request, 'admin_imoveis.html')

def tiposimoveis(request):
    return render(request, 'admin_tipos_imoveis.html')

def detalhesimovel(request):
    return render(request, 'detalhes_imovel.html')

def mensagens(request):
    return render(request, 'mensagens.html')

def estatisticas(request):
    return render(request, 'estatisticas.html')