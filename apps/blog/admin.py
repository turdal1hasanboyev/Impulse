from django.contrib import admin

from apps.blog.models import Blog, travelImages


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", 'updated_at')
    prepopulated_fields = {"slug": ["name"]}


@admin.register(travelImages)
class travelImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'updated_at')
