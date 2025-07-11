from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'category', 'price', 'publish_status', 'owner')
    list_display = ('id', 'name', 'price', 'category','publish_status', 'owner')
    list_filter = ('category', 'publish_status', 'owner')
    search_fields = ('name', 'description',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
