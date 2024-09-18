from django.urls import path 
from .views import (
    HomeView,
    CartView,
    ProductView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
]
