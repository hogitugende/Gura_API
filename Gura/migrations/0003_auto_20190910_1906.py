# Generated by Django 2.2.3 on 2019-09-10 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gura', '0002_auto_20190903_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profil',
            name='tel',
            field=models.CharField(max_length=15, unique=True, verbose_name='numero de téléphone'),
        ),
    ]
