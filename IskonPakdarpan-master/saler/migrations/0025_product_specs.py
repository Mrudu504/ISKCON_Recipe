# Generated by Django 3.2 on 2021-08-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0024_remove_product_specs'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
