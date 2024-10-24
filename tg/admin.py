from django.contrib import admin
from .models import tgCard, tgCategory, countVisitTg

@admin.register(tgCategory)
class TgCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(tgCard)
class TgCardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(countVisitTg)
class countVisitTgAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')
    list_filter = ['views']
    search_fields= ['views']