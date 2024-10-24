from django.contrib import admin
from .models import Books, CategoryBook

@admin.register(Books)
class TgCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(CategoryBook)
class TgCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
   		