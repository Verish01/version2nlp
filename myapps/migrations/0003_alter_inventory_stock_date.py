# Generated by Django 5.0.6 on 2024-05-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0002_inventory_delete_inventorydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock_date',
            field=models.DateField(),
        ),
    ]
