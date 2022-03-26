from pyexpat import model
from django.contrib import admin
from basket.models import BasketInline, Basket

# Register your models here.


class BasketInline(admin.TabularInline):
    model = BasketInline
    extra = 1


class BasketAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketInline,)


admin.site.register(Basket, BasketAdmin)
