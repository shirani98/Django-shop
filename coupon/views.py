from django.shortcuts import redirect
from django.views.generic import View
from .models import CouponModel
from .forms import CouponForm 
from django.utils.timezone import datetime
from order.models import Order
# Create your views here.

class CouponRun(View):
    
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get('id')
        form = CouponForm(request.POST)
        now = datetime.now()
        if form.is_valid():
            cd = form.cleaned_data
            if CouponModel.objects.filter(code__exact= cd['code'], from_date__lt = now, to_date__gt = now).exists() :
                query = CouponModel.objects.get(code__exact= cd['code'], from_date__lt = now, to_date__gt = now)
                submit_coupon = Order.objects.get(id = order_id)
                submit_coupon.discount_amount = query.discount
                submit_coupon.save()
        return redirect('order:detail', order_id )