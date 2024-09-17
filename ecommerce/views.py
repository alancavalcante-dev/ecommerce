from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import json
from datetime import datetime as dt

def consulta(request, url):
    return (
        requests.get(
            url, 
            headers = {
                'Authorization': f'Bearer {request.session.get('access_token')}'
            }
        )
    )
     


class LoginView(generic.View):
    
    def get(self, request):
    
        return render(
            request, 
            'ecommerce/login.html'
        )
    
    def post(self, request):
        get_token = "http://127.0.0.1:8000/api/v1/authentication/token/"

        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        response = requests.post(get_token, json=data)
        print(response)
        if response.status_code == 200:
            tokens = response.json()
            request.session['access_token'] = tokens['access']
            request.session['refresh_token'] = tokens['refresh']  
            return redirect('home')

        return render(
            request, 
            'ecommerce/login.html', {
                'error': 'Usuário ou senha inválidos'
            }
        )

        
    

class RegisterView(generic.View):
    
    def get(self, request):
        return render(
            request, 
            'ecommerce/register.html'
        )




class HomeView(generic.View):
    
    def get(self, request):
        teste = consulta(request, 'http://127.0.0.1:8000/api/v1/products/')

        teste = teste.json()

        for i in teste:
            try:
                if i['release_date']:
                    i['release_date'] = dt.strptime(i['release_date'][:10], '%Y-%m-%d').date()
            except:
                teste = []
                break
        return render(
            request, 
            'ecommerce/home.html', {
                'teste': teste,
                'tam_teste' : len(teste) if not 'detail' in teste else 0
            }
        )
    



class CartView(LoginRequiredMixin, generic.View):
    
    def get(self, request):
        return render(
            request, 
            'ecommerce/cart.html'
        )


