from rest_framework import serializers
from accounts.models import User
from shop.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.title')
    type = serializers.CharField(source='type.title')
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'brand', 'type',
                  'image', 'body', 'price', 'created')

    def get_category(self, obj):
        return obj.category.all().values('title')


class ProductAddSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('title', 'category', 'brand',
                  'type', 'image', 'body', 'price')


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
