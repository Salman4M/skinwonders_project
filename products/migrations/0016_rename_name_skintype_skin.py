# Generated by Django 3.2 on 2023-09-06 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_skintype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skintype',
            old_name='name',
            new_name='skin',
        ),
    ]