from typing import Mapping
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, DetailView

from wallet.models import Transaction, TransactionsArchive, Transfer, UserBalance
from .models import Product
from cart.forms import AddToCardForm
from django.contrib.postgres.search import SearchVector
from .session import Visited 
from django.conf import settings
from redis import Redis
# Create your views here.

redis_con = Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB,decode_responses=True)       

class ShopView(ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.filter(is_active = True)
    paginate_by = 8
        

class ProductView(DetailView):
    template_name = 'shop/detail.html'
    model = Product
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['quantity_form'] = AddToCardForm
        context['related_product'] = Product.objects.filter(category__title = self.object.category.first()).exclude(slug = self.kwargs['slug']).order_by('?') [:4]
        return context
    
    
    
class Search(ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Product.objects.annotate(search =SearchVector('title', 'body'), ).filter(search = q)
    
