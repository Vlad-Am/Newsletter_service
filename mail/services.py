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
    newsletter_list = Newsletter.objects.all().filter(status="created")
    for newsletter in newsletter_list:
        if newsletter.datetime_start_send <= current_datetime < newsletter.datetime_end_send:

            newsletter.status = 'started'
            newsletter.save()
            emails_list = [client.email for client in newsletter.client.all()]

            try:
                answer = send_mail(
                    subject=newsletter.message.subject,
                    message=newsletter.message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=emails_list,
                    fail_silently=False,
                )
                status = 'Отправлено'
                log = Logs(newsletter=newsletter, status=status, answer=answer)
                log.save()

            except smtplib.SMTPException as error:
                status = "Не отправлено"
                answer = f'Ошибка отправки {error}'
                log = Logs(newsletter=newsletter, status=status, answer=answer)
                log.save()

            day = timedelta(days=1)
            weak = timedelta(days=7)
            month = timedelta(days=30)

            if newsletter.frequency == 'daily':
                newsletter.datetime_start_send = log.time_last_send + day
                newsletter.save()
            elif newsletter.frequency == 'weekly':
                newsletter.datetime_start_send = log.time_last_send + weak
            elif newsletter.frequency == 'monthly':
                newsletter.datetime_start_send = log.time_last_send + month

            if newsletter.datetime_start_send < newsletter.datetime_end_send:
                newsletter.status = 'created'
            else:
                newsletter.status = 'done'
            newsletter.save()
