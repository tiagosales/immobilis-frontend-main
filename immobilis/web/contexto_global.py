from .utils import is_user_logged_in

def variaveis_globais(request):
    return {
        'api_url': 'http://localhost:5000',
        'base_url': 'http://localhost:5000/api/v1/',
    }

def user_id(request):
    if is_user_logged_in(request):
        return {'user_id': request.session.get('user_id'),'access_token': request.session.get('access_token')}
    else:
        return {'user_id': 0}
