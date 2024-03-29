# Generated by Django 4.0.4 on 2022-06-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0065_rename_name_teachers_absence_teacher_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='boy',
            name='kind',
            field=models.CharField(choices=[('2', 'انثى'), ('1', 'ذكر')], default='1', max_length=50, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='boy',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='month',
            field=models.CharField(blank=True, choices=[('7', 'يوليو'), ('8', 'أغسطس'), ('3', 'مارس'), ('9', 'سبتمبر'), ('11', 'نوفمبر'), ('10', 'أكتوبر'), ('5', 'مايو'), ('1', 'يناير'), ('4', 'أبريل'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('2', 'فبراير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.CharField(choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='month',
            field=models.CharField(blank=True, choices=[('7', 'يوليو'), ('8', 'أغسطس'), ('3', 'مارس'), ('9', 'سبتمبر'), ('11', 'نوفمبر'), ('10', 'أكتوبر'), ('5', 'مايو'), ('1', 'يناير'), ('4', 'أبريل'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('2', 'فبراير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('7', 'يوليو'), ('8', 'أغسطس'), ('3', 'مارس'), ('9', 'سبتمبر'), ('11', 'نوفمبر'), ('10', 'أكتوبر'), ('5', 'مايو'), ('1', 'يناير'), ('4', 'أبريل'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('2', 'فبراير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('7', 'يوليو'), ('8', 'أغسطس'), ('3', 'مارس'), ('9', 'سبتمبر'), ('11', 'نوفمبر'), ('10', 'أكتوبر'), ('5', 'مايو'), ('1', 'يناير'), ('4', 'أبريل'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('2', 'فبراير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='techers',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='techers',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('تكتك', 'تكتك'), ('سيارة', 'سيارة'), ('اتوبيس', 'اتوبيس'), ('ميكروباس', 'ميكروباس')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2023', '2023-2024'), ('2022', '2022-2023')], max_length=50, null=True),
        ),
    ]
