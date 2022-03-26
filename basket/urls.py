from basket.views import AddToBasket, BasketDetail, DeleteBasket
from django.urls import path

app_name = 'basket'

urlpatterns = [
    path('add/', AddToBasket.as_view(), name='add'),
    path('detail/', BasketDetail.as_view(), name='detail'),
    path('del/<int:product_id>', DeleteBasket.as_view(), name = 'del'),

]