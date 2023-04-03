from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    context = {}
    return render(request, 'app/register.html', context)
def login(request):
    context = {}
    return render(request, 'app/login.html', context)
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        # cartItems = order.get_get_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        # cartItems = order['get_cart_items']
    products = Prodcut.objects.all()
    context={'products' : products}
    return render(request, 'app/home.html', context)
def product(request):
    context = {}
    return render(request, 'app/product.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        # cartItems = order.get_get_items

    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        # cartItems = order['get_cart_items']
    context={'items':items,'order':order}
    return render(request, 'app/cart.html', context)
def checkout(request):
    context={}
    return render(request, 'app/checkout.html', context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Prodcut.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('added', safe=False)