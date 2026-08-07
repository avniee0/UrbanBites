from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from core.models import MenuItem

from django.shortcuts import render, redirect
from orders.models import Order
from core.models import MenuItem
from django.shortcuts import get_object_or_404


def dashboard_home(request):

    orders = Order.objects.all().order_by('-created_at')

    total_orders = orders.count()


    total_revenue = 0

    for order in orders:
        total_revenue += order.total_price


    total_items = MenuItem.objects.count()


    pending_orders = orders.filter(
        status='Pending'
    ).count()


    return render(
        request,
        'dashboard/dashboard.html',
        {
            'total_orders': total_orders,
            'total_revenue': total_revenue,
            'total_items': total_items,
            'pending_orders': pending_orders,
            'recent_orders': orders[:5],
        }
    )

def update_order_status(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == "POST":

        status = request.POST.get("status")

        order.status = status
        order.save()

    return redirect('dashboard')

def menu_manage(request):

    menu_items = MenuItem.objects.all()

    return render(
        request,
        'dashboard/menu_manage.html',
        {
            'menu_items': menu_items
        }
    )

def add_menu_item(request):

    if request.method == "POST":

        name = request.POST.get("name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES.get("image")


        MenuItem.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            image=image
        )


        return redirect('menu_manage')


    return render(
        request,
        'dashboard/add_item.html'
    )
def edit_menu_item(request, id):

    item = MenuItem.objects.get(id=id)


    if request.method == "POST":

        item.name = request.POST.get("name")
        item.category = request.POST.get("category")
        item.description = request.POST.get("description")
        item.price = request.POST.get("price")


        if request.FILES.get("image"):
            item.image = request.FILES.get("image")


        item.save()


        return redirect('menu_manage')


    return render(
        request,
        'dashboard/edit_item.html',
        {
            'item': item
        }
    )
def delete_menu_item(request, id):

    item = MenuItem.objects.get(id=id)

    item.delete()

    return redirect('menu_manage')

def order_manage(request):

    orders = Order.objects.all().order_by('-created_at')

    return render(
        request,
        'dashboard/order_manage.html',
        {
            'orders': orders
        }
    )