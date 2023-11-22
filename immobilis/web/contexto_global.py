from .utils import is_user_logged_in
from immobilis.settings import URL_BACKEND

def variaveis_globais(request):
    return {
        'api_url': URL_BACKEND,
        'base_url': URL_BACKEND+'/api/v1/',
    }

def user_id(request):
    if is_user_logged_in(request):
        return {'user_id': request.session.get('user_id'),'access_token': request.session.get('access_token')}
    else:
        return {'user_id': 0}
