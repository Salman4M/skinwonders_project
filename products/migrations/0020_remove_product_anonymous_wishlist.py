# Generated by Django 3.2 on 2023-09-09 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_anonymous_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='anonymous_wishlist',
        ),
    ]
