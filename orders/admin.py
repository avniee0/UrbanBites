from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'customer_name',
        'phone',
        'total_price',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )