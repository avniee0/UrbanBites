from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import Cart


def checkout(request):

    items = Cart.objects.all()

    if not items.exists():
        return redirect('cart')


    total = 0

    for item in items:
        total += item.total_price()


    if request.method == "POST":

        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']


        # Create Order
        order = Order.objects.create(
            customer_name=name,
            phone=phone,
            address=address,
            total_price=total
        )


        # Save ordered items
        for cart_item in items:

            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity
            )


        # Clear cart
        Cart.objects.all().delete()


        return render(
            request,
            'orders/success.html',
            {
                'order': order
            }
        )


    return render(
        request,
        'orders/checkout.html',
        {
            'items': items,
            'total': total
        }
    )