# Generated by Django 4.2 on 2024-04-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0008_alter_newsletter_datetime_start_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='datetime_start_send',
            field=models.DateTimeField(null=True, verbose_name='Дата и время начала рассылки'),
        ),
    ]
