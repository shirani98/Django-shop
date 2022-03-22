from django.contrib import admin
from .models import Product, ProductAttribute, ProductAttributeValue, ProductType
# Register your models here.
class ProductAttrValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','price','is_active','created')
    list_filter = ( 'category' , 'is_active', 'created',)
    search_fields = ('title','body')
    list_editable = ('is_active','price')
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ProductAttrValueInline,)
    fieldsets = (
        ('Main', {'fields': ('title','slug','category','brand','type')}),
        ('Description', {'fields': ('body', 'image')}),
        ('Detail', {'fields': ('price','is_active',)}),
    )
    actions = ['make_is_active']
    def make_is_active(self, request, queryset):
        update =queryset.update(is_active=True)
        self.message_user(request,f"{update} rows updated")

admin.site.register(Product, ProductAdmin)

class ProductAttrInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1
    
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = (ProductAttrInline,)
admin.site.register(ProductType,ProductTypeAdmin)

