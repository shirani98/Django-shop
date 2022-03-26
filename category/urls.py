from django.urls import path
from .views import ShowCatProduct


app_name = 'category'

urlpatterns = [
    path('<slug:slug>/', ShowCatProduct.as_view(), name='catlist'),

]
