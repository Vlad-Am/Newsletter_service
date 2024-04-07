from django import forms
from django.db import models

from users.models import User


class Message(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    subject = models.TextField(verbose_name='Тема письма')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Сообщение:{self.message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, max_length=254, verbose_name='Электронная почта')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True, blank=True)

    def __str__(self):
        return f'Пользователь {self.surname} {self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    FREQUENCY_CHOICES = [
        (DAILY, 'раз в день'),
        (WEEKLY, 'раз в неделю'),
        (MONTHLY, 'раз в месяц'),
    ]

    CREATED = 'created'
    STARTED = 'started'
    DONE = 'done'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Активная'),
        (DONE, 'Завершена'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True, blank=True)
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания рассылки', null=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='Частота рассылки')
    status = models.CharField(max_length=10, default=CREATED, choices=STATUS_CHOICES, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', null=True)
    client = models.ManyToManyField(Client, verbose_name='Адресаты рассылки')
    datetime_start_send = models.DateTimeField(verbose_name='Дата и время начала рассылки ГГГГ-ММ-ДД ЧЧ:MM')
    datetime_end_send = models.DateTimeField(verbose_name='Дата и время окончания рассылки ГГГГ-ММ-ДД ЧЧ:MM')
    is_active = models.BooleanField(default=True, verbose_name='Активная')

    def __str__(self):
        return f'Сообщение:{self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('set_is_activated', 'Может отключать рассылку')
        ]


class Logs(models.Model):
    time_last_send = models.DateTimeField(auto_now=True, verbose_name='Дата и время последней попытки')
    status = models.TextField(verbose_name='Статус')
    answer = models.TextField(verbose_name='Ответ сервера')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка', null=True)

    def __str__(self):
        return f'''Сообщение:{self.newsletter}\nСтатус:{self.status}\nОтвет:{self.answer}'''
    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'
