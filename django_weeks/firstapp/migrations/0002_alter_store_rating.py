# Generated by Django 4.0.5 on 2022-07-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
