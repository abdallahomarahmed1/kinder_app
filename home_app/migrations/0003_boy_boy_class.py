# Generated by Django 3.2.6 on 2021-08-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_classes_techers'),
    ]

    operations = [
        migrations.AddField(
            model_name='boy',
            name='boy_class',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='home_app.classes', verbose_name='افصل'),
            preserve_default=False,
        ),
    ]