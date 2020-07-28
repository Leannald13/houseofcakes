from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H9saXHQmyytvvuzZdiUPu88c1Sh8Ljhb0TmTeDRbQJvK1YNZ6WjsGboDxAGaTx9xTlCJrNeNY34eq8J2RnoYicV00wfRXpJkx',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
