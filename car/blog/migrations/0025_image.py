# Generated by Django 5.0.7 on 2024-10-25 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_signup_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='post_images/')),
                ('title', models.CharField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post')),
            ],
            options={
                'ordering': ['-title'],
                'indexes': [models.Index(fields=['title', 'date_created'], name='blog_image_title_12aef5_idx')],
            },
        ),
    ]