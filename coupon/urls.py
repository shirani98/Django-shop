from django.urls import path
from .views import CouponRun


app_name = 'coupon'

urlpatterns = [
    path('check/<int:id>', CouponRun.as_view(), name = 'check'),

]