# Generated by Django 5.1.5 on 2025-03-16 08:12

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_delete_student_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام گروه')),
                ('code', models.SmallIntegerField(default=0, verbose_name='کد گروه')),
            ],
        ),
        migrations.CreateModel(
            name='lesson_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_day', models.CharField(choices=[('شنبه', 'شنبه'), ('یکشنبه', 'یکشنبه'), ('دوشنبه', 'دوشنبه'), ('سه شنبه', 'سه شنبه'), ('چهارشنبه', 'چهارشنبه'), ('پنج شنبه', 'پنج شنبه')], default='شنبه', max_length=10, verbose_name='روز برگزاری کلاس')),
                ('lesson_time', models.CharField(max_length=100, verbose_name='ساعت برگزاری')),
                ('capacity', models.SmallIntegerField(verbose_name='ظرفیت')),
                ('class_code', models.SmallIntegerField(verbose_name='کد ارائه')),
                ('class_number', models.SmallIntegerField(verbose_name='شماره کلاس')),
                ('semester', models.SmallIntegerField(verbose_name='نیمسال')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('modified', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='classes', to='website.group', verbose_name='نام گروه')),
                ('lesson_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='classes', to='website.lesson', verbose_name='نام درس')),
                ('professor_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='classes', to='website.professor', verbose_name='نام استاد')),
                ('university_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='classes', to='website.university', verbose_name='مکان برگزاری')),
            ],
        ),
    ]
