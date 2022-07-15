# Generated by Django 4.0.4 on 2022-06-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0060_staff_number_kawme_staff_number_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_absence',
            name='name',
        ),
        migrations.AddField(
            model_name='monthly_exams',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='boy',
            name='kind',
            field=models.CharField(choices=[('2', 'انثى'), ('1', 'ذكر')], default='1', max_length=50, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='boy',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='boy',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='month',
            field=models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('9', 'سبتمبر'), ('2', 'فبراير'), ('7', 'يوليو'), ('8', 'أغسطس'), ('6', 'يونيو'), ('3', 'مارس'), ('4', 'أبريل'), ('10', 'أكتوبر'), ('11', 'نوفمبر'), ('5', 'مايو'), ('1', 'يناير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.CharField(choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='month',
            field=models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('9', 'سبتمبر'), ('2', 'فبراير'), ('7', 'يوليو'), ('8', 'أغسطس'), ('6', 'يونيو'), ('3', 'مارس'), ('4', 'أبريل'), ('10', 'أكتوبر'), ('11', 'نوفمبر'), ('5', 'مايو'), ('1', 'يناير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم الموظف'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('9', 'سبتمبر'), ('2', 'فبراير'), ('7', 'يوليو'), ('8', 'أغسطس'), ('6', 'يونيو'), ('3', 'مارس'), ('4', 'أبريل'), ('10', 'أكتوبر'), ('11', 'نوفمبر'), ('5', 'مايو'), ('1', 'يناير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('12', 'ديسمبر'), ('9', 'سبتمبر'), ('2', 'فبراير'), ('7', 'يوليو'), ('8', 'أغسطس'), ('6', 'يونيو'), ('3', 'مارس'), ('4', 'أبريل'), ('10', 'أكتوبر'), ('11', 'نوفمبر'), ('5', 'مايو'), ('1', 'يناير')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='techers',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='techers',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('اتوبيس', 'اتوبيس'), ('سيارة', 'سيارة'), ('تكتك', 'تكتك'), ('ميكروباس', 'ميكروباس')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='year',
            field=models.CharField(blank=True, choices=[('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024'), ('2021', '2021-2022')], max_length=50, null=True),
        ),
    ]
