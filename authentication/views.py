from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
import requests



class LoginView(generic.View):
    
    def get(self, request):
    
        return render(
            request, 
            'authentication/login.html'
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
            return redirect('home')

        return render(
            request, 
            'ecommerce/login.html', {
                'error': 'Usuário ou senha inválidos'
            }
        )

        

class LogoutView(generic.View):
    
    def get(self, request):
        logout(request)
        return redirect('home')
    

class RegisterView(generic.View):
    
    def get(self, request):
        return render(
            request, 
            'authentication/register.html'
        )
    


class RetrieveView(generic.View):
    
    def get(self, request):
        return render(
            request, 
            'authentication/retrieve.html'
        )
