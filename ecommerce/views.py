from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import json


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

        if response.status_code == 200:
            tokens = response.json()
            request.session['access_token'] = tokens['access']
            request.session['refresh_token'] = tokens['refresh']  
            print(request.session['access_token'])
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
        return render(
            request, 
            'ecommerce/home.html'
        )
    



class CartView(LoginRequiredMixin, generic.View):
    
    def get(self, request):
        return render(
            request, 
            'ecommerce/cart.html'
        )


