from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    """Model representig store"""
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be beetween 1 and 100"),
            MaxValueValidator(100, message="Rating must be beetween 1 and 100")]
    )

    def __str__(self):
        return f"{self.name} - {self.rating}"
