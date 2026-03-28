from django.db import models

# Create your models here.

class Artwork(models.Model):

    CATEGORY_CHOICES = [
        ('OIL', 'Oil'),
        ('ACRYLIC', 'Acrylic'),
        ('WATERCOLOR', 'Watercolor'),
        ('MIXED', 'Mixed Media'),
    ]

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)

    image = models.CharField(max_length=500)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    description = models.TextField(blank=True)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title