from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
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

    cart[item_id] = quantity
    messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Allow user to remove item from the cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('cart', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['cart'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
