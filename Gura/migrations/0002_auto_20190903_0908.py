# Generated by Django 2.2.3 on 2019-09-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='adresse',
            field=models.CharField(max_length=15, null=True, verbose_name='adresse'),
        ),
        migrations.AddField(
            model_name='profil',
            name='ville',
            field=models.CharField(max_length=15, null=True, verbose_name='ville'),
        ),
    ]
