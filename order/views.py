from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, RedirectView

from basket.models import Basket
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models import Product
from coupon.forms import CouponForm
# Create your views here.


class OrderDetail(LoginRequiredMixin,  DetailView):
    model = Order
    template_name = 'order/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CouponForm()
        return context


class AddOrder(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.get(id=self.request.COOKIES.get("basket_id"))
        order = Order.objects.create(user=request.user)
        for item in basket.basket_inline.all():
            order_item = OrderItem.objects.create(
                order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        return redirect('order:detail', order.id)
