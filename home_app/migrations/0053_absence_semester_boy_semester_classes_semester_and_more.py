# Generated by Django 4.0.4 on 2022-05-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0052_darajat_ejamly_darajat_darajat_ejamly_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='boy',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='classes',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='darajat',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='driver',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='masrof',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='mawad',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='profile',
            name='semester',
            field=models.CharField(choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], default=1, max_length=50, verbose_name='الفصل الدراسي'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='techers',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AddField(
            model_name='transport',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'الفصل الدراسي الاول'), ('second', 'الفصل الدراسي الثاني')], max_length=50, null=True, verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='kind',
            field=models.CharField(choices=[('سيارة', 'سيارة'), ('ميكروباس', 'ميكروباس'), ('اتوبيس', 'اتوبيس'), ('تكتك', 'تكتك')], max_length=50, verbose_name='نوع وسيلة النقل'),
        ),
    ]
