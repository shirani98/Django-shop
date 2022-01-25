from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length= 200, unique=True)
    category = models.ManyToManyField(Category, related_name='category')
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
            
