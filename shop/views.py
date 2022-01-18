from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.
class ShopView(ListView):
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    template_name = 'shop/index.html'
    
class ProductView(DetailView):
    template_name = 'shop/detail.html'
    model = Product