from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from order.models import Order

# Create your models here.


class CouponModel(models.Model):
    code = models.CharField(max_length=15)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    @classmethod
    def check_coupon(cls, order_id, form, now):
        if form.is_valid():
            cd = form.cleaned_data
            if cls.objects.filter(code__exact=cd['code'], from_date__lt=now, to_date__gt=now).exists():
                query = cls.objects.get(
                    code__exact=cd['code'], from_date__lt=now, to_date__gt=now)
                submit_coupon = Order.objects.get(id=order_id)
                submit_coupon.discount_amount = query.discount
                submit_coupon.save()
        return order_id
