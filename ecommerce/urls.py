from django.urls import path 
from .views import (
    HomeView,
    CartView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart/', CartView.as_view(), name='cart'),
]
