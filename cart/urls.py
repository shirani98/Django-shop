from django.urls import path
from .views import CardDetail, AddToCart, DeleteCart


app_name = 'cart'


urlpatterns  = [
    path('add/<int:product_id>', AddToCart.as_view(), name = 'add'),
    path('del/<int:product_id>', DeleteCart.as_view(), name = 'del'),
    path('', CardDetail.as_view(), name = 'detail'),

]