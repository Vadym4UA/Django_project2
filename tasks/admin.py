from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'deadline', 'status', 'priority')
    list_filter = ('status', 'category', 'priority')
    search_fields = ('title', 'description')
    date_hierarchy = 'deadline'
    ordering = ('-priority', 'deadline')