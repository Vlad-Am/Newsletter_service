# Generated by Django 4.2 on 2024-04-06 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0010_remove_newsletter_count_send_logs_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='client',
        ),
    ]
