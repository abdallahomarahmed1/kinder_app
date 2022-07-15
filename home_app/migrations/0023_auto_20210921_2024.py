# Generated by Django 3.2.7 on 2021-09-21 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0022_auto_20210921_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='darajat',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_app.boy', verbose_name='اسم الطالب'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('tok tok', 'tok tok'), ('car', 'car'), ('bus', 'bus')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
