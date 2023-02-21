from django.contrib import admin
from .models import Cuisine

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
