from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CouponModel
from .forms import CouponForm 
from django.utils.timezone import datetime
from order.models import OrderItem
# Create your views here.

class CouponRun(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('id')
        form = CouponForm(request.POST)
        now = datetime.now()
        
        if form.is_valid():
            cd = form.cleaned_data
            query = CouponModel.objects.get(code__exact= cd['code'], from_date__lt = now, to_date__gt = now)
            if query :
                get_order = OrderItem.objects.get(order__id = product_id)
                get_order.price = (get_order.price * query.discount) / 100
                get_order.save()
        return redirect('order:detail', product_id )