# Generated by Django 4.0.4 on 2022-05-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0051_alter_transport_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='darajat',
            name='ejamly_darajat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='darajat',
            name='ejamly_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='darajat',
            name='nesba',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
