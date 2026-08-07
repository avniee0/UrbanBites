from django.shortcuts import redirect, render, get_object_or_404
from core.models import MenuItem
from .models import Cart


def add_to_cart(request, id):

    item = get_object_or_404(MenuItem, id=id)

    cart_item, created = Cart.objects.get_or_create(
        item=item
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')



def cart_view(request):

    items = Cart.objects.all()

    total = 0

    for item in items:
        total += item.total_price()

    return render(
        request,
        'cart/cart.html',
        {
            'items': items,
            'total': total
        }
    )



# Increase quantity

def increase_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')



# Decrease quantity

def decrease_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')



# Remove item

def remove_item(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    cart_item.delete()

    return redirect('cart')