# Generated by Django 5.2.4 on 2025-07-23 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='ip-адресс')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Публикация')),
            ],
        ),
    ]
