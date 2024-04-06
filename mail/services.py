import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from mail.models import Newsletter, Logs


def send_mail_by_time():
    """Отправка письма по времени"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    day = timedelta(days=1)
    weak = timedelta(days=7)
    month = timedelta(days=30)
    newsletter_list = Newsletter.objects.all().filter(status='Cоздана')
    print(newsletter_list)
    for newsletter in newsletter_list:
        if newsletter.time_start <= current_datetime < newsletter.time_end:

            newsletter.status = 'Активная'
            newsletter.save()
            emails_list = [client.email for client in newsletter.client.all()]

            try:
                send_mail(
                    subject=newsletter.message.subject,
                    message=newsletter.message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=emails_list,
                    fail_silently=False,
                )
                status = 'Отправлено'
            except smtplib.SMTPException as error:
                status = f'Ошибка отправки {error}'

            log = Logs(newsletter=newsletter, status=status)
            log.save()

            if newsletter.frequency == 'раз в день':
                newsletter.datetime_start_send = log.time_last_send + day
            elif newsletter.frequency == 'раз в неделю':
                newsletter.datetime_start_send = log.time_last_send + weak
            elif newsletter.frequency == 'раз в месяц':
                newsletter.datetime_start_send = log.time_last_send + month

            if newsletter.datetime_start_send < newsletter.datetime_end_send:
                newsletter.status = 'Создана'
            else:
                newsletter.status = 'Завершена'
            newsletter.save()
