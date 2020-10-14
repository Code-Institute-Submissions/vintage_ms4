from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart content"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add the specified product to the shopping Cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated quantity of donations to {product.name} (Total: {cart[item_id]})')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)
