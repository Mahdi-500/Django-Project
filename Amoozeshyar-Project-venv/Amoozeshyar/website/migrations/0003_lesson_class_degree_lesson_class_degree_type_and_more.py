# Generated by Django 5.1.5 on 2025-05-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_professor_website_pro_profess_dc4420_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_class',
            name='degree',
            field=models.CharField(choices=[('کارشناسی', 'کارشناسی'), ('ارشد', 'کارشناسی ارشد'), ('دکتری', 'دکتری')], default='کارشناسی', max_length=8, verbose_name='مقطع'),
        ),
        migrations.AddField(
            model_name='lesson_class',
            name='degree_type',
            field=models.CharField(choices=[('پیوسته', 'پیوسته'), ('ناپیوسته', 'ناپیوسته')], default='پیوسته', max_length=8, verbose_name='نوع مقطع'),
        ),
        migrations.AlterField(
            model_name='lesson_class',
            name='lesson_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یک', 'یکشنبه'), ('دو', 'دوشنبه'), ('سه', 'سه شنبه'), ('چهار', 'چهارشنبه'), ('پنج', 'پنج شنبه')], default='شنبه', max_length=4, verbose_name='روز برگزاری کلاس'),
        ),
    ]
