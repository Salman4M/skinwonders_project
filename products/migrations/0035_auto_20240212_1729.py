# Generated by Django 3.2 on 2024-02-12 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20240212_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_tr',
            new_name='name_az',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_tr',
            new_name='name_az',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='skin_tr',
            new_name='skin_az',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='status_tr',
            new_name='status_az',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_tr',
            new_name='title_az',
        ),
    ]
