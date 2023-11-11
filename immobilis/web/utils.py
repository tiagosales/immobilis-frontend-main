import requests, json
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def user_id(request):
    if is_user_logged_in(request):
        return {'user_id': request.session.get('user_id')}
    else:
        return {'user_id': 0}

@csrf_exempt
def login_post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Realizar a autenticação através da API Flask
        headers = {'Accept': 'application/json','Content-Type': 'application/json'}
        response = requests.post('http://127.0.0.1:5000/api/v1/auth/login', data=json.dumps({'email': email, 'senha': senha}),headers=headers)

        if response.status_code == 200:
            data = response.json()
            user_id = data.get('user_id')
            perfil_id = data.get('perfil_id')
            access_token = data.get('access_token')

            # Criar e salvar a sessão do usuário
            session = SessionStore()
            session['user_id'] = user_id
            session['perfil_id'] = perfil_id
            session['access_token'] = access_token
            session.create()

            # Definir o cookie de sessão no navegador
            response = JsonResponse({'message': 'Login realizado com sucesso!'})
            response.set_cookie(key='sessionid', value=session.session_key, httponly=True)
            return response
        else:
            return JsonResponse({'message': 'Falha no login. Verifique suas credenciais e tente novamente.'}, status=401)
    else:
        return JsonResponse({'message': 'Método não permitido.'}, status=405)

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
    response = redirect('login')
    response.delete_cookie('sessionid')
    return response