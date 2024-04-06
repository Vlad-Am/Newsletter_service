from time import sleep

from django.apps import AppConfig


class MailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail'

    def ready(self):
        from mail.services import send_mail_by_time
        sleep(2)
        send_mail_by_time()
