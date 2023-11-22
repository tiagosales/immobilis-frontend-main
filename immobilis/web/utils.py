import requests, json
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from immobilis.settings import URL_BACKEND
import traceback

def user_id(request):
    if is_user_logged_in(request):
        return {'user_id': request.session.get('user_id')}
    else:
        return {'user_id': 0}

@csrf_exempt
def login_process(request):
    if request.method == 'GET':
        req_id_token = request.GET.get('id_token')
        user_id = request.GET.get('user_id')
        perfil_id = request.GET.get('perfil_id')
        access_token = request.GET.get('access_token')
        if not verify_google_access_token(req_id_token):
            return JsonResponse({'message': 'Falha no login. Verifique suas credenciais e tente novamente.'}, status=401)
        
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Realizar a autenticação através da API Flask
        headers = {'Accept': 'application/json','Content-Type': 'application/json'}
        responselogin = requests.post(URL_BACKEND+'/api/v1/auth/login', data=json.dumps({'email': email, 'senha': senha}),headers=headers)

        if responselogin.status_code == 200 or responselogin.status_code == 201:
            data = responselogin.json()
            user_id = data.get('user_id')
            perfil_id = data.get('perfil_id')
            access_token = data.get('access_token')
        else:
            return JsonResponse({'message': 'Falha no login. Verifique suas credenciais e tente novamente.'}, status=401)
    else:
        return JsonResponse({'message': 'Método não permitido.'}, status=405)
    
    # Criar e salvar a sessão do usuário
    session = SessionStore()
    session['user_id'] = user_id
    session['perfil_id'] = perfil_id
    session['access_token'] = access_token
    session.create()
    
    # Definir o cookie de sessão no navegador
    response = JsonResponse({'message': 'Login realizado com sucesso!'},status=responselogin.status_code)
    #response = redirect('/busca/')
    response.set_cookie(key='sessionid', value=session.session_key, httponly=True)
    return response


def is_user_logged_in(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key:
        try:
            session = Session.objects.get(session_key=session_key)
            user_id = session.get_decoded().get('user_id')
            if user_id:
                return True
        except Session.DoesNotExist:
            pass
    return False

def logout(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key:
        try:
            session = Session.objects.get(session_key=session_key)
            session.delete()
        except Session.DoesNotExist:
            pass
    response = redirect(URL_BACKEND+'/logout')
    response.delete_cookie('sessionid')
    return response


def verify_google_access_token(req_id_token):
    try:
        idinfo = id_token.verify_oauth2_token(
            req_id_token, grequests.Request())

        # Verifique se o 'iss' (emissor) é o Google
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return False

        return True
    except:
        traceback.print_exc()
        return False