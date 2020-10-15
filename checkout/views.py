from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HRghCKvKuGGOibTXxmZxLxFIOztxDJrzmZXrtONcjfMBiy8GfvXyrdPrvS75SBH3O71GhY0IPl4BUHiAgS2A3UA00fu0XFm5J',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
