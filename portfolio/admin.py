from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'date_completed']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'tech_stack']
    list_filter = ['featured']
