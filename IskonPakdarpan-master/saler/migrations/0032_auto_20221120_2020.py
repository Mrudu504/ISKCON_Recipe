# Generated by Django 2.2.14 on 2022-11-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0031_auto_20221120_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='products/images'),
        ),
    ]
