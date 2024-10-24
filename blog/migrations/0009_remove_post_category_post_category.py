# Generated by Django 5.0.1 on 2024-10-22 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='blog.postcategory'),
        ),
    ]
