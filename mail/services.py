import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from mail.models import Logs, Newsletter


def send_mail_by_time():
    """Отправка письма по времени"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    newsletter_list = Newsletter.objects.all().filter(status="created")
    for newsletter in newsletter_list:
        if (
            newsletter.datetime_start_send
            <= current_datetime
            < newsletter.datetime_end_send
        ):

            newsletter.status = "started"
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
                status = "Отправлено"
                log = Logs(newsletter=newsletter, status=status, answer=answer)
                log.save()

            except smtplib.SMTPException as error:
                status = "Не отправлено"
                answer = f"Ошибка отправки {error}"
                log = Logs(newsletter=newsletter, status=status, answer=answer)
                log.save()

            day = timedelta(days=1)
            weak = timedelta(days=7)
            month = timedelta(days=30)

            if newsletter.frequency == "daily":
                newsletter.datetime_start_send = log.time_last_send + day
            elif newsletter.frequency == "weekly":
                newsletter.datetime_start_send = log.time_last_send + weak
            elif newsletter.frequency == "monthly":
                newsletter.datetime_start_send = log.time_last_send + month

            if newsletter.datetime_start_send < newsletter.datetime_end_send:
                newsletter.status = "created"
            else:
                newsletter.status = "done"
            newsletter.save()


def get_cache_for_mailings():
    if settings.CACHE_ENABLED:
        mailings_count = Newsletter.objects.all().count()
    else:
        key = "mailings_count"
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Newsletter.objects.all().count()
            cache.set(key, mailings_count)
    return mailings_count


def get_cache_for_active_mailings():
    if settings.CACHE_ENABLED:
        active_mailings_count = Newsletter.objects.filter(is_active=True).count()
    else:
        key = "active_mailings_count"
        active_mailings_count = cache.get(key)
        if active_mailings_count is None:
            active_mailings_count = Newsletter.objects.filter(is_active=True).count()
            cache.set(key, active_mailings_count)
    return active_mailings_count
