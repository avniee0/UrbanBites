from django.db import models
from core.models import MenuItem


class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    total_price = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.customer_name



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.item.name