from ecommerce.views import consulta

def custom_context(request):
    try:
        response = consulta(request, 'me/').json()
        username = response[0]['username']
    except:
        username = False


    return {
        'username': username
    }