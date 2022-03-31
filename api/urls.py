from django.urls import path
from api.views import AccountsChangePassView, AccountsRegisterView, ProductCatrgoryList, ProductCreateView, ProductActionView, ProductListView, ProductDetailView


app_name = 'Api'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/cat/<str:category>/', ProductCatrgoryList.as_view(), name='category-list'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/action/<int:pk>/', ProductActionView.as_view(), name='action'),
    path('accounts/register/', AccountsRegisterView.as_view(), name='register'),
    path('accounts/passupdate/', AccountsChangePassView.as_view(), name='passupdate'),

]