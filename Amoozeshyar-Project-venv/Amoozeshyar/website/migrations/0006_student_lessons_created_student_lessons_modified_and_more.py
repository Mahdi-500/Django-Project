# Generated by Django 5.1.5 on 2025-03-13 11:13

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_student_lessons_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_lessons',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='student_lessons',
            name='modified',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ تغییر'),
        ),
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.TextField(default='تهران', verbose_name='آدرس'),
        ),
    ]
