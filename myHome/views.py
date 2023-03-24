from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'myHome/index.html')

def products(request):
    products = Product.objects.filter(manage=request.user)
    context = {'products':products} 
    return  render(request,'myHome/cart.html',context)

def about(request):
    return render(request, 'myhome/about.html')

def contact(request):
   return render(request, 'myhome/contact.html')  

def blog(request):
    return render(request, 'myhome/blog.html')    

def serve(request):
   return render(request, 'myhome/services.html') 

def sell(request):
   return render(request, 'myhome/sell.html')    
    
def buy(request):
    return render(request, 'myhome/Buy.html')    
    
def cart(request):
    return render(request, 'myhome/cart.html')    

def productlist(request):
    return render(request, 'myhome/product.html')

