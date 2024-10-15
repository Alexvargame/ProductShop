from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','amount','active')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display=('product','image')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=('title',)



