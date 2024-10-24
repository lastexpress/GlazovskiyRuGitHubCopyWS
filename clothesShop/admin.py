from django.contrib import admin
from .models import CategoryClothes, Product

# Register your models here.
@admin.register(CategoryClothes)
class CategoryClothes(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class Product(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}