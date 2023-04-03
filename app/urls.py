from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('cart/', views.cart, name="cart"),
    path('product/', views.cart, name="product"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),


]
