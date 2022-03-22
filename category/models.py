from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=250, unique=True)
    sub_cat = models.ForeignKey('self',on_delete = models.CASCADE, null= True, blank=True, related_name='selfcat')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category:catlist', kwargs={'slug': self.slug})
        
        
class Brand (models.Model):
    title = models.CharField(max_length=200)           
    
    def __str__(self):
        return self.title