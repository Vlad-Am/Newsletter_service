
from django.contrib import admin

from mail.models import Newsletter, Message, Client, Logs


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "subject",)
    list_filter = ("subject",)
    search_fields = ("subject",)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("owner", "datetime_start_send", "frequency", "status", "message",)
    list_filter = ("owner", "frequency", "status", "message", "client","datetime_start_send")
    search_fields = ("message", "owner", "client",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email",)
    list_filter = ("email",)
    search_fields = ("surname", "email",)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('time_last_send', 'status', 'answer', "newsletter",)
