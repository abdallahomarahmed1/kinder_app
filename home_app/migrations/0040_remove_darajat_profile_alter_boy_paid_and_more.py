# Generated by Django 4.0.1 on 2022-05-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0039_darajat_profile_alter_transport_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='darajat',
            name='profile',
        ),
        migrations.AlterField(
            model_name='boy',
            name='paid',
            field=models.IntegerField(verbose_name='المبلغ المدفوع'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('ميكروباس', 'ميكروباس'), ('اتوبيس', 'اتوبيس'), ('سيارة', 'سيارة'), ('تكتك', 'تكتك')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]