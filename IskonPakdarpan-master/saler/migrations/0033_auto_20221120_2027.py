# Generated by Django 2.2.14 on 2022-11-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0032_auto_20221120_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
