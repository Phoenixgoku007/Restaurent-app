from django.contrib import admin
from .models import Review


class ReviewInline(admin.TabularInline):
    model = Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'rating', 'created_on')
    list_filter = ('restaurant', 'rating')