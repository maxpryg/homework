from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    """Model representig store"""
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    owner = models.ForeignKey('auth.User', related_name='stores', null=True,
                              blank=True, on_delete=models.SET_NULL)
    store_status = [
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
        ('in_review', 'In review'),
    ]
    status = models.CharField(max_length=12,
                              choices=store_status, default='in_review')

    def __str__(self):
        return f"{self.name} - {self.rating}"
