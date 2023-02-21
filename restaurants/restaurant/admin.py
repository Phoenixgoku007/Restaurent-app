from django.contrib import admin
from .models import Restaurant
from dish.models import Dish
from review.models import Review
from bookmark.models import Bookmark
from visit.models import Visit

class DishInline(admin.StackedInline):
    model = Dish

class ReviewInline(admin.StackedInline):
    model = Review

class BookmarkInline(admin.StackedInline):
    model = Bookmark

class VisitInline(admin.StackedInline):
    model = Visit

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [DishInline, ReviewInline, BookmarkInline, VisitInline]
    list_display = ('title', 'cuisine', 'location')
    list_filter = ('cuisine', 'location')
    search_fields = ('title', 'description', 'location')
