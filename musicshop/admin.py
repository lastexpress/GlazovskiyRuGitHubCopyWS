from django.contrib import admin
# from .models import Member, Genre, Artist, Album
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import *

@admin.register(PageVisit)
class countVisitTgAdmin(admin.ModelAdmin):
    list_display = ('name', 'visits')
    list_filter = ['visits']
    search_fields= ['visits']