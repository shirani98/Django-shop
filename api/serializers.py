from rest_framework import serializers
from accounts.models import User
from shop.models import Product

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.title') 
    type = serializers.CharField(source='type.title') 
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'brand', 'type', 'image', 'body', 'price', 'created')
        
    def get_category(self, obj):
        return obj.category.all().values('title')
    
class ProductAddSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('title','category', 'brand', 'type', 'image', 'body', 'price' )
        
    def get_image (self, obj):
        return obj.url
    
class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email','phone', 'password')
        
    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],
            validated_data['email'],validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    