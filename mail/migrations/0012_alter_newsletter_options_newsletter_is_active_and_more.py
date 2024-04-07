# Generated by Django 4.2 on 2024-04-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0011_remove_logs_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('set_is_activated', 'Может отключать рассылку')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AddField(
            model_name='newsletter',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='datetime_end_send',
            field=models.DateTimeField(verbose_name='Дата и время окончания рассылки ГГГГ-ММ-ДД ЧЧ:MM'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='datetime_start_send',
            field=models.DateTimeField(verbose_name='Дата и время начала рассылки ГГГГ-ММ-ДД ЧЧ:MM'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('created', 'Создана'), ('started', 'Активная'), ('done', 'Завершена')], default='created', max_length=10, verbose_name='Статус рассылки'),
        ),
    ]
