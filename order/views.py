from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, RedirectView
from .models import Order , OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.sessions import Cart
from shop.models import Product
# Create your views here.

class OrderDetail(LoginRequiredMixin ,  DetailView):
    model = Order
    template_name = 'order/detail.html'
    

class AddOrder(LoginRequiredMixin , View):
    def get(self , request, *args, **kwargs):
        cart = Cart(request)
        order = Order.objects.create(user = request.user)
        for item in cart :
            order_item = OrderItem.objects.create(order = order , product = item['product'] , price = item['price'] , number = item['number'])
        cart.clean()
        return redirect('order:detail' , order.id )
    