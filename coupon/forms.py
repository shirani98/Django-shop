from django import forms

class CouponForm(forms.Form):
    code = forms.CharField(max_length=15, label ='Coupon')