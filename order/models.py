from django.db import models
from home.models import UserProfile
from gallery.models import Artwork

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=500)
    pincode = models.CharField(max_length=10)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    payment_status = models.CharField(max_length=20, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)