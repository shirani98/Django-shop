from django.shortcuts import render
from rest_framework import generics
from accounts.models import User
from api.serializers import ChangePasswordSerializer, ProductListSerializer, ProductAddSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from shop.models import Product
from rest_framework.response import Response
from rest_framework import status
from api.models import create_user_api, update_password_api

# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer


class ProductCatrgoryList(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.filter(category__title=self.kwargs.get('category'))


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer


class ProductCreateView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductAddSerializer
    permission_classes = (IsAdminUser,)


class ProductActionView(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductListSerializer
    permission_classes = (IsAdminUser,)


class AccountsRegisterView(generics.CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        return create_user_api(self.get_serializer(data = request.data))


class AccountsChangePassView(generics.UpdateAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        return update_password_api(self.get_object(),self.get_serializer(data=request.data))