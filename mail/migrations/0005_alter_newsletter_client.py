# Generated by Django 4.2 on 2024-04-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_remove_client_newsletter_newsletter_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ManyToManyField(to='mail.client', verbose_name='Адресаты рассылки'),
        ),
    ]
