# Generated by Django 5.1.1 on 2024-09-25 05:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar_app', '0008_remove_product_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
