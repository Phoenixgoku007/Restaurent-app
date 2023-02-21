from django.contrib import admin
from .models import Visit

class VisitInline(admin.TabularInline):
    model = Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'created_on')
    list_filter = ('restaurant',)