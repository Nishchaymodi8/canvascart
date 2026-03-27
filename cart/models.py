# cart/models.py

from django.db import models
from home.models import UserProfile
from gallery.models import Artwork

class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.artwork.price
    
    class Meta:
        unique_together = ('user', 'artwork')