import requests
from  web.contexto_global import variaveis_globais,user_id
from datetime import datetime

class AccessLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        base_url = variaveis_globais(request)['base_url']
        user_info = user_id(request)

        # Registre o acesso na API Flask
        acesso_data = {
            'id_usuario': user_info['user_id'],
            'data_acesso': datetime.now().isoformat(),
            'caminho': request.get_full_path()
        }

        # Faça a solicitação POST para a API Flask
        response_flask_api = requests.post(base_url+'acessos/', json=acesso_data)

        # Retorne a resposta original
        return response