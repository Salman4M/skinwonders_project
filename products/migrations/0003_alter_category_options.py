# Generated by Django 3.2 on 2023-09-03 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created_at',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
