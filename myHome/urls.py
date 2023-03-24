from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    
    path("about/", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("blog", views.blog, name="Blog"),
    path("service", views.serve, name="Services"),
    path("sell", views.sell, name="Sell"),
    path("buy", views.buy, name="Buy"),
    path("productlist", views.productlist, name="ProductList"),
    path("cart", views.cart, name="Cart"),
]