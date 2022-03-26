from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from accounts.models import User
from shop.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='basket', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.id} "

    def get_quantity(self, data_form):
        form = data_form(self.request.POST)
        if form.is_valid():
            quantity_form = form.cleaned_data['quantity']
        return quantity_form

    @classmethod
    def add_user(cls, self):
        if self.request.user.is_authenticated:
            basket = get_object_or_404(
                cls, id=self.request.COOKIES.get('basket_id'))
            if basket.user is not None and basket.user != self.request.user:
                raise Http404
            basket.user = self.request.user
            basket.save()
            return basket
        return None

    @classmethod
    def create_basket(cls, self):
        if self.request.user.is_authenticated:
            return Basket.objects.create(user=self.request.user)
        return Basket.objects.create()

    @classmethod
    def submit(cls, self, response, quantity_form):
        if self.request.COOKIES.get('basket_id') is not None:
            cls.add_user(self)
            return BasketInline.add(self.request.POST.get('product_id'), self.request.COOKIES.get('basket_id'), quantity_form)
        basket = cls.create_basket(self)
        BasketInline.add(self.request.POST.get(
            'product_id'), basket.id, quantity_form)
        return response.set_cookie('basket_id', basket.id)


class BasketInline(models.Model):
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name='basket_inline')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()

    @classmethod
    def add(cls, product_id, basket_id, quantity):
        product = get_object_or_404(Product, id=product_id)
        basket = get_object_or_404(Basket, id=basket_id)
        basket_in = cls.objects.filter(basket=basket, product=product)
        if basket_in.exists():
            basket_in = cls.objects.get(basket=basket, product=product)
            basket_in.quantity += quantity
            basket_in.save()
        else:
            cls.objects.create(
                basket=basket, product=product, quantity=quantity)
