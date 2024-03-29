# Generated by Django 4.0.4 on 2022-05-29 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0056_boy_date_of_birth_boy_addres_boy_allergy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='techers',
            name='Reward',
            field=models.IntegerField(blank=True, null=True, verbose_name='المكافأة السنوية'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='boy',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='month',
            field=models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('5', 'مايو'), ('4', 'أبريل'), ('6', 'يونيو'), ('2', 'فبراير'), ('7', 'يوليو'), ('3', 'مارس'), ('11', 'نوفمبر'), ('9', 'سبتمبر'), ('1', 'يناير'), ('8', 'أغسطس'), ('10', 'أكتوبر')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='techers',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('تكتك', 'تكتك'), ('اتوبيس', 'اتوبيس'), ('ميكروباس', 'ميكروباس'), ('سيارة', 'سيارة')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='year',
            field=models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Teachers_absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('5', 'مايو'), ('4', 'أبريل'), ('6', 'يونيو'), ('2', 'فبراير'), ('7', 'يوليو'), ('3', 'مارس'), ('11', 'نوفمبر'), ('9', 'سبتمبر'), ('1', 'يناير'), ('8', 'أغسطس'), ('10', 'أكتوبر')], max_length=50, null=True)),
                ('year', models.CharField(blank=True, choices=[('2022', '2022-2023'), ('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024')], max_length=50, null=True)),
                ('excuse', models.BooleanField(default=False, verbose_name='بعذر')),
                ('the_reason', models.CharField(blank=True, max_length=50, null=True, verbose_name='السبب')),
                ('add_date', models.DateField(blank=True, null=True, verbose_name='التاريخ')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home_app.techers', verbose_name='اسم المدرس')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.profile', verbose_name='المستخدم')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
        ),
    ]
