# Generated by Django 3.0.2 on 2020-08-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0003_auto_20200819_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
