from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from cart.forms import AddToCardForm
from django.contrib.postgres.search import SearchVector
from random import randint
# Create your views here.
class ShopView(ListView):
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    template_name = 'shop/index.html'
    
class ProductView(DetailView):
    template_name = 'shop/detail.html'
    model = Product
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['form'] = AddToCardForm
        return context
    
class Search(ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Product.objects.annotate(search =SearchVector('title', 'body'), ).filter(search = q)
    
