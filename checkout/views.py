from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})

            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
            )

                order_line_item.save()

                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined!")
 
            if customer.paid:
                messages.error(request, "You have successfully paid!")
                request.session['cart'] = {}
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take payment!")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    context = {
        'order_form': OrderForm,
        'payment_form': MakePaymentForm,
        'stripe_public_key': stripe_public_key
    }

    return render(request, 'checkout/checkout.html', context)

