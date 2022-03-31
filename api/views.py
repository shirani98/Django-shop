from django.shortcuts import render
from rest_framework import generics
from accounts.models import User
from api.serializers import ProductListSerializer, ProductAddSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAdminUser
from shop.models import Product

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductListSerializer
    
class ProductCatrgoryList(generics.ListAPIView):
    serializer_class = ProductListSerializer
    
    def get_queryset(self):
        return Product.objects.filter(category__title = self.kwargs.get('category'))
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductListSerializer

    
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializer
    permission_classes = (IsAdminUser,)
    
        
class ProductActionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (IsAdminUser,)
    
class AccountsRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
#class AccountsLoginView(generics.CreateAPIView):
    

    