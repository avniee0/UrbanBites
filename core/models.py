from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu/')

    def __str__(self):
        return self.name



class Order(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )


    customer_name = models.CharField(max_length=100)

    item = models.CharField(max_length=100)

    amount = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.customer_name