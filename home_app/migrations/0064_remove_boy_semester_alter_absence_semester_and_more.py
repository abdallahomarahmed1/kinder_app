# Generated by Django 4.0.4 on 2022-06-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0063_alter_absence_year_alter_boy_kind_alter_boy_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boy',
            name='semester',
        ),
        migrations.AlterField(
            model_name='absence',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='boy',
            name='allergy',
            field=models.BooleanField(blank=True, default=False, verbose_name='لديه حساسية'),
        ),
        migrations.AlterField(
            model_name='boy',
            name='sick',
            field=models.BooleanField(blank=True, default=False, verbose_name='يعناي الطفل من امراض اخرى'),
        ),
        migrations.AlterField(
            model_name='boy',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='darajat',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='mawad',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='month',
            field=models.CharField(blank=True, choices=[('11', 'نوفمبر'), ('9', 'سبتمبر'), ('3', 'مارس'), ('1', 'يناير'), ('7', 'يوليو'), ('2', 'فبراير'), ('4', 'أبريل'), ('5', 'مايو'), ('10', 'أكتوبر'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('8', 'أغسطس')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='monthly_exams',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.CharField(choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='month',
            field=models.CharField(blank=True, choices=[('11', 'نوفمبر'), ('9', 'سبتمبر'), ('3', 'مارس'), ('1', 'يناير'), ('7', 'يوليو'), ('2', 'فبراير'), ('4', 'أبريل'), ('5', 'مايو'), ('10', 'أكتوبر'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('8', 'أغسطس')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('11', 'نوفمبر'), ('9', 'سبتمبر'), ('3', 'مارس'), ('1', 'يناير'), ('7', 'يوليو'), ('2', 'فبراير'), ('4', 'أبريل'), ('5', 'مايو'), ('10', 'أكتوبر'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('8', 'أغسطس')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='month',
            field=models.CharField(blank=True, choices=[('11', 'نوفمبر'), ('9', 'سبتمبر'), ('3', 'مارس'), ('1', 'يناير'), ('7', 'يوليو'), ('2', 'فبراير'), ('4', 'أبريل'), ('5', 'مايو'), ('10', 'أكتوبر'), ('12', 'ديسمبر'), ('6', 'يونيو'), ('8', 'أغسطس')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_absence',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='techers',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='techers',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('سيارة', 'سيارة'), ('اتوبيس', 'اتوبيس'), ('تكتك', 'تكتك'), ('ميكروباس', 'ميكروباس')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='semester',
            field=models.CharField(blank=True, choices=[('second', 'الفصل الدراسي الثاني'), ('first', 'الفصل الدراسي الاول')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='year',
            field=models.CharField(blank=True, choices=[('2021', '2021-2022'), ('2024', '2024-2025'), ('2022', '2022-2023'), ('2023', '2023-2024')], max_length=50, null=True),
        ),
    ]
