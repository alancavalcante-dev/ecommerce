from ecommerce.views import consulta

def custom_context(request):
    try:
        response, token = consulta(request, 'me/', return_token=True)
        username = response.json()[0]['username']
    except:
        username = False
        token = ''



    return {
        'username': username,
        'token': token
    }