# Generated by Django 4.0.1 on 2022-01-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0032_rename_date_absence_created_alter_transport_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('tok tok', 'تكتك'), ('hafela', 'ميكروباس'), ('car', 'سيارة'), ('bus', 'اتوبيس')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]