from django.db import models

from users.models import User


class Message(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    subject = models.TextField(verbose_name='Тема письма')

    def __str__(self):
        return f'Сообщение:{self.message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Newsletter(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    datetime = models.DateField(auto_now_add=True, verbose_name='Дата создания рассылки', null=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='Частота рассылки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', null=True)

    def __str__(self):
        return f'Сообщение:{self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    newsletter = models.ManyToManyField(Newsletter, verbose_name='Сообщения', blank=True)

    def __str__(self):
        return f'Пользователь {self.surname} {self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Logs(models.Model):
    time_last_send = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.IntegerField(verbose_name='Статус')
    answer = models.TextField(verbose_name='Ответ сервера')



