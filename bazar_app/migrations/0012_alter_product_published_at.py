# Generated by Django 5.1.1 on 2024-09-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar_app', '0011_product_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
