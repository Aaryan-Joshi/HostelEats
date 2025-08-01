# menu/views.py
from django.shortcuts import render, redirect
from .models import MenuItem, Order, OrderItem

def index(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/index.html', {'menu_items': menu_items})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('index')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for item_id, qty in cart.items():
        menu_item = MenuItem.objects.get(id=item_id)
        items.append({'item': menu_item, 'quantity': qty, 'subtotal': menu_item.price * qty})
        total += menu_item.price * qty
    return render(request, 'menu/cart.html', {'items': items, 'total': total})

from django.shortcuts import render, redirect
from .models import MenuItem, Order, OrderItem

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    if request.method == 'POST':
        try:
            name = request.POST['customer_name']
            phone = request.POST['phone_number']
            hostel = request.POST['hostel_name']
            room = request.POST['room_number']
        except KeyError:
            error = "Please fill in all details."
            return render(request, 'menu/checkout.html', {'error': error})

        # Create the order without any item
        order = Order.objects.create(
            customer_name=name,
            phone_number=phone,
            hostel_name=hostel,
            room_number=room
        )

        # Create order items linked to the order
        for item_id_str, qty in cart.items():
            item_id = int(item_id_str)
            menu_item = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(
                order=order,
                item=menu_item,
                quantity=qty
            )

        # Clear the cart
        request.session['cart'] = {}

        return render(request, 'menu/order_success.html', {'order': order})

    # For GET request, display the checkout form
    return render(request, 'menu/checkout.html')


def order_success(request):
    # Render order success page
    return render(request, 'menu/order_success.html')
