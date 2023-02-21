from django.contrib import admin
from .models import Dish


class DishInline(admin.TabularInline):
    model = Dish

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)