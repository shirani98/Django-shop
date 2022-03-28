from django.urls import path
from .views import ShopView, ProductView, Search


app_name = 'shop'


urlpatterns = [
    path('', ShopView.as_view(), name='index'),
    path('detail/<slug:slug>/', ProductView.as_view(), name='detail'),
    path('search/', Search.as_view(), name='search'),

]
