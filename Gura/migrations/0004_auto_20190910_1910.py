# Generated by Django 2.2.3 on 2019-09-10 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gura', '0003_auto_20190910_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
