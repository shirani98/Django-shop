from django.shortcuts import redirect
from django.views.generic import View
from .models import CouponModel
from .forms import CouponForm
from django.utils.timezone import datetime
# Create your views here.


class CouponRun(View):

    def post(self, request, *args, **kwargs):
        order_id = CouponModel.check_coupon(self.kwargs.get(
            'id'), CouponForm(request.POST), datetime.now())
        return redirect('order:detail', order_id)
