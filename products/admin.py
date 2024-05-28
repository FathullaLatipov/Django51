from django.contrib import admin

from .models import CategoryModel, ProductModel


# Создаем админ панель для категории
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title', 'price']
    list_display = ['id', 'title', 'price', 'count', 'updated_at', 'created_at']
    list_filter = ['created_at']