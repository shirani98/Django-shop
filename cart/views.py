from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .sessions import Cart
from shop.models import Product
from .forms import AddToCardForm

# Create your views here.

class CardDetail(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request,'cart/cart.html',{'cart' : cart})
    
class AddToCart(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id = self.kwargs['product_id'])
        form = AddToCardForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, number=cd['number'])
            
        return redirect('cart:detail')
    
class DeleteCart(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product , id = kwargs.get('product_id'))
        cart.delete(product)
        return redirect('cart:detail')
