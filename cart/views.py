from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import MenuItem
from .models import Cart

# Add item to cart
@login_required(login_url='login')
def add_to_cart(request, id):

    item = get_object_or_404(MenuItem, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        item=item
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


# Show cart
@login_required(login_url='login')
def cart_view(request):

    items = Cart.objects.filter(user=request.user)

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
@login_required(login_url='login')
def increase_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id, user=request.user)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


# Decrease quantity
@login_required(login_url='login')
def decrease_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')


# Remove item
@login_required(login_url='login')
def remove_item(request, id):

    cart_item = get_object_or_404(Cart, id=id, user=request.user)

    cart_item.delete()

    return redirect('cart')