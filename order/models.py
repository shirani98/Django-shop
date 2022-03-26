from django.db import models
from django.conf import settings
from django.db.models import Sum
from shop.models import Product
from django.db.models import F
# Create your models here.


class Order (models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    discount_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.id}"

    def get_total(self, *args, **kwargs):
        total = self.items.all().aggregate(total=Sum(F('price')*F('quantity')))
        if self.discount_amount:
            return (total['total'] - (total['total'] * self.discount_amount / 100))
        return total['total']


class OrderItem (models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
