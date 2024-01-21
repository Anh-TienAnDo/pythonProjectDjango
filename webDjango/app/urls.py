from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home),
    path('cart/', views.Cart, name="cart"),
    path('checkout/', views.Checkout, name="checkout"),
    path('login/', views.Login, name="login"),
    path('singup/', views.Singup, name="signup"),
]
