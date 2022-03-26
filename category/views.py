from django.views.generic import ListView
from shop.models import Product
# Create your views here.


class ShowCatProduct(ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        return Product.objects.filter(category__title=self.kwargs['slug'])
