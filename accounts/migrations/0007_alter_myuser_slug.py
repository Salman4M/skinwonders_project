# Generated by Django 3.2 on 2023-09-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]