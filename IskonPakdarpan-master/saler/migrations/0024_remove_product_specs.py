# Generated by Django 3.2 on 2021-08-10 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0023_product_specs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specs',
        ),
    ]
