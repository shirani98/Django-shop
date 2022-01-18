from django.shortcuts import render
from django.views.generic import ListView
from .models import Category
from shop.models import Product
# Create your views here.
class ShowCatProduct(ListView):
    def get_queryset(self):
        return Product.objects.filter(category__title= self.kwargs['slug'])
    template_name = 'shop/index.html'
    