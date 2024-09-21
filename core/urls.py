from django.contrib import admin
from django.urls import path, include
from authentication.views import (
    LoginView,
    RegisterView,
    RetrieveView
)


# carrinho
# ecommerce
# minha conta
# minhas compras
# help => FAQ - Perguntas Frequentes, Pagamentos, Devolução e Reembolso, 
# Informações Gerais, Quem somos, Vendedores e Parceiros
# chat

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('retrieve/', RetrieveView.as_view(), name='retrieve'),

    path('', include('ecommerce.urls')),

]


