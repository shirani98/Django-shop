from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.http import HttpResponseRedirect
from basket.forms import AddToCardForm
from basket.models import Basket, BasketInline
from shop.models import Product

# Create your views here.


class AddToBasket(View):

    def post(self, *args, **kwargs):
        response = HttpResponseRedirect(self.request.POST.get('next', '/'))
        Basket.submit(self, response, Basket.get_quantity(self, AddToCardForm))
        return response


class BasketDetail(View):

    def get(self, request, *args, **kwargs):
        if self.request.COOKIES.get("basket_id"):
            basket = Basket.objects.get(
                id=self.request.COOKIES.get("basket_id"))
            return render(request, 'basket/basket.html', {'cart': basket.basket_inline.all()})
        return render(request, 'basket/basket.html', {'cart': []})


class DeleteBasket(View):

    def get(self, request, *args, **kwargs):
        get_product = get_object_or_404(Product, id=kwargs.get('product_id'))
        basket = Basket.objects.get(id=self.request.COOKIES.get("basket_id"))
        BasketInline.objects.filter(
            basket=basket, product=get_product).delete()
        return redirect('basket:detail')
