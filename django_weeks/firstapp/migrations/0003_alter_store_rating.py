# Generated by Django 4.0.5 on 2022-07-04 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_store_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Rating must be beetween 1 and 100'), django.core.validators.MaxValueValidator(100, message='Rating must be beetween 1 and 100')]),
        ),
    ]
