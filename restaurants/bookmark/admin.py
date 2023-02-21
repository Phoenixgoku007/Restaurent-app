from django.contrib import admin
from .models import Bookmark

class BookmarkInline(admin.TabularInline):
    model = Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'created_on')
    list_filter = ('restaurant__title',)