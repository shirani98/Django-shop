from pyexpat import model
import uuid
from django.db import models
from category.models import Brand, Category
from django.urls import reverse
# Create your models here.
class ProductType(models.Model):
    title = models.CharField(max_length= 200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class ProductAttribute(models.Model):
    product_attribute = ((1,'integer'),(2,'string'),(3,'float'))
    
    title = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="attr")
    attributes = models.SmallIntegerField(default = 1, choices =product_attribute)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length= 200, unique=True)
    category = models.ManyToManyField(Category, related_name='category')
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE,related_name='brand')
    type = models.ForeignKey(ProductType, on_delete = models.CASCADE, related_name='type')
    image = models.ImageField(upload_to = 'images/product/%y/%m/%d')
    body = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    is_active = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'slug' : self.slug})
    

class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE, related_name='attr_value')
    value = models.CharField(max_length= 200)
    attributes = models.ForeignKey(ProductAttribute, on_delete= models.CASCADE, related_name='value')    
    
    def __str__(self):
        return f"{self.product} {self.attributes} : {self.value}"
    
