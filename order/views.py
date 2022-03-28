from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
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
        order = OrderItem.add_order_item(self.request.COOKIES.get("basket_id"),request.user)
        return redirect('order:detail', order.id)
