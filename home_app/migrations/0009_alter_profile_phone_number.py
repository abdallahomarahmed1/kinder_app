# Generated by Django 3.2.6 on 2021-08-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_auto_20210818_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم الهاتف'),
        ),
    ]
