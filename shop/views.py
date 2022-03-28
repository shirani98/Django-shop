from django.views.generic import ListView, DetailView
from .models import Product
from basket.forms import AddToCardForm
from django.contrib.postgres.search import SearchVector
from django.conf import settings
# Create your views here.


class ShopView(ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.filter(is_active=True)
    paginate_by = 8


class ProductView(DetailView):
    template_name = 'shop/detail.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['quantity_form'] = AddToCardForm
        context['related_product'] = Product.objects.filter(
            category__title=self.object.category.first()).exclude(slug=self.kwargs['slug']).order_by('?')[:4]
        return context


class Search(ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Product.objects.annotate(search=SearchVector('title', 'body'), ).filter(search=q)
