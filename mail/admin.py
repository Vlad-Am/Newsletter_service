
from django.contrib import admin

from mail.models import Newsletter, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "subject",)
    list_filter = ("subject",)
    search_fields = ("subject",)


@admin.register(Newsletter)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("owner", "datetime", "frequency", "status", "message",)
    list_filter = ("owner", "frequency", "status", "message",)
    search_fields = ("message", "owner",)


