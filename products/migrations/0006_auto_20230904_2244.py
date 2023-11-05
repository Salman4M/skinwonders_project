# Generated by Django 3.2 on 2023-09-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230903_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW IN', 'NEW IN'), ('LOW STOCK', 'LOW STOCK')], max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='SkinType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('product', models.ManyToManyField(blank=True, to='products.Product')),
            ],
        ),
    ]