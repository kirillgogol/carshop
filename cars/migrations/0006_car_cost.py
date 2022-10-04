# Generated by Django 4.1 on 2022-09-06 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cost',
            field=models.IntegerField(default=10000, validators=[django.core.validators.MaxValueValidator(2000000), django.core.validators.MinValueValidator(10000)]),
        ),
    ]