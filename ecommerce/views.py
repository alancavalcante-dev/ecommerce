from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from datetime import datetime as dt

def consulta_token(request) -> bool:
    """
    Consulta se o token está autenticado "Validado"
    """
    body = {'token': request.session.get('access_token')}
    response = requests.post('http://127.0.0.1:8000/api/v1/authentication/token/verify/', json=body)
    if response.status_code == 200:
        return True
    else:
        return False







def consulta(request, url=False, return_token=False):
    url_base = 'http://127.0.0.1:8000/api/v1/' + url
    if not consulta_token(request):
        if return_token: 
            return requests.get(url_base), []
        else:
            return requests.get(url_base)
    else:
        access_token = request.session.get('access_token')
        response = requests.get(
                url_base, 
                headers = {'Authorization': f'Bearer {access_token}'}
            )  
        if return_token:
            return response, access_token
        return response
    
    
     





class HomeView(generic.View):
    
    def get(self, request):
        search = request.GET.get('search') 


        response = consulta(
            request, 
            'products/' + f'?search={search}' if search else 'products/'
        ).json()
        
        for i in response:
            try:
                if i['release_date']:
                    i['release_date'] = dt.strptime(i['release_date'][:10], '%Y-%m-%d').date()
            except:
                response = []
                break
        return render(
            request, 
            'ecommerce/home.html', {
                'response': response,
                'tam_response' : len(response) if not 'detail' in response else 0
            }
        )
    



class CartView(generic.View):
    
    def get(self, request):
        validation = consulta_token(request)
        if not validation:
            return redirect('login')

        response = consulta(request, 'cart/').json()

        return render(
            request, 
            'ecommerce/cart.html', {
                'items': response
            }
        )
    



class ProductView(generic.View):

    def get(self, request, pk):
        if request.session.get('access_token'):
            response, token = consulta(request, f'products/{pk}/', return_token=True)
        else:
            response = consulta(request, f'products/{pk}/')
            token = ''
        
        return render(
            request,
            'ecommerce/product.html', {
                'product': response.json(),
                'token': token
            }
        )



class UserView(generic.View):

    def get(self, request, pk):
        if request.session.get('access_token'):
            response, token = consulta(request, f'products/{pk}/', return_token=True)
        else:
            response = consulta(request, f'products/{pk}/')
            token = ''
        
        return render(
            request,
            'ecommerce/product.html', {
                'product': response.json(),
                'token': token
            }
        )
    



class ProfileView(generic.View):

    def get(self, request):
        validation = consulta_token(request)
        if not validation:
            return redirect('login')
        response = consulta(request, 'me/').json()
        
        for i in response:
            response = {
                'username': i['username'],
                'first_name': i['first_name'],
                'last_name': i['last_name'],
                'email': i['email'],
                'password': i['password']
            }
        return render(
            request,
            'ecommerce/profile.html', {
                'profile': response,
            }
        )
