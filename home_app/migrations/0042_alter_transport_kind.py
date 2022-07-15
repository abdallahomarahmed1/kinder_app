# Generated by Django 4.0.4 on 2022-05-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0041_darajat_profile_alter_transport_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('اتوبيس', 'اتوبيس'), ('ميكروباس', 'ميكروباس'), ('سيارة', 'سيارة'), ('تكتك', 'تكتك')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
