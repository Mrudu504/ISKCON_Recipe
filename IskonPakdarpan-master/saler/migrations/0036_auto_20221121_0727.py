# Generated by Django 2.2.14 on 2022-11-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0035_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaleproduct',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='products/images'),
        ),
    ]
