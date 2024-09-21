from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from datetime import datetime as dt

def consulta_token(request) -> bool:
    body = {'token': request.session.get('access_token')}
    response = requests.post('http://127.0.0.1:8000/api/v1/authentication/token/verify/', json=body)
    if response.status_code == 200:
        return True
    else:
        return False







def consulta(request, url=False):
    url_base = 'http://127.0.0.1:8000/api/v1/' + url
    return (
        requests.get(
            url_base, 
            headers = {
                'Authorization': f'Bearer {request.session.get('access_token')}'
            }
        )
    )
     





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

        return render(
            request, 
            'ecommerce/cart.html'
        )



class ProductView(generic.View):

    def get(self, request, pk):
        response = consulta(request, f'products/{pk}/')

        return render(
            request,
            'ecommerce/product.html', {
                'product': response.json()
            }
        )
