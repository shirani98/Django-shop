from typing import Mapping
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product
from cart.forms import AddToCardForm
from django.contrib.postgres.search import SearchVector
from .session import Visited 
from django.conf import settings
from redis import Redis
# Create your views here.

redis_con = Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB,decode_responses=True)       
class ShopView(ListView):
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    template_name = 'shop/index.html'
    
    def setup(self, request, *args, **kwargs):
        self.view =  redis_con.zrevrangebyscore("view","+inf" , "-inf")[:4]
        return super().setup(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['view'] = [get_object_or_404(Product, id = int(item)) for item in self.view]
        print("*"*50)
        print(context['view'])
        context['product_visited'] = list(Visited(self.request))
        return context
class ProductView(DetailView):
    template_name = 'shop/detail.html'
    model = Product
    
    def setup(self, request, *args, **kwargs):
        visited = Visited(request)
        product = Product.objects.get(slug = kwargs['slug'])
        visited.add(product)
        return super().setup(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['form'] = AddToCardForm
        context['related_product'] = Product.objects.filter(category__title = self.object.category.all()[0]).exclude(slug = self.kwargs['slug']) [:4]
        context['view'] = int(redis_con.zincrby("view" , 1 , self.object.id))
        return context
    
    
class Search(ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Product.objects.annotate(search =SearchVector('title', 'body'), ).filter(search = q)
    
