from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "view_count",
        "created_at",
    )
    list_filter = (
        "created_at",
        "view_count",
    )
    search_fields = ("title", "content")
