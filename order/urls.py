from django.urls import path
from .views import OrderDetail, AddOrder
app_name = 'order'

urlpatterns = [
    path("create/", AddOrder.as_view(), name="add"),
    path("<int:pk>/", OrderDetail.as_view(), name="detail"),

]
