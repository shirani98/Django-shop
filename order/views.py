from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, RedirectView
from .models import Order , OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.sessions import Cart
from shop.models import Product
from coupon.forms import CouponForm
# Create your views here.

class OrderDetail(LoginRequiredMixin ,  DetailView):
    model = Order
    template_name = 'order/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CouponForm()
        return context
    

class AddOrder(LoginRequiredMixin , View):
    
    def get(self , request, *args, **kwargs):
        cart = Cart(request)
        order = Order.objects.create(user = request.user)
        for item in cart :
            order_item = OrderItem.objects.create(order = order , product = item['product'] , price = item['price'] , quantity = item['quantity'])
        cart.clean()
        return redirect('order:detail' , order.id )
    