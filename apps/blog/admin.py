from django.contrib import admin

from apps.blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", 'updated_at')
    prepopulated_fields = {"slug": ["name"]}
