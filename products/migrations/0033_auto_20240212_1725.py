# Generated by Django 3.2 on 2024-02-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20240212_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
