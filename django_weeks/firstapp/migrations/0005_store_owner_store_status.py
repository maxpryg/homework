# Generated by Django 4.0.5 on 2022-07-10 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0004_alter_store_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('deactivated', 'deactivated'), ('in_review', 'in_review')], default='active', max_length=12),
        ),
    ]
