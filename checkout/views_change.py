from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm, Order
from .models import OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

import stripe
import json


# def checkout(request):
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY

#     if request.method == 'POST':
#         cart = request.session.get('cart', {})

#         form_data = {
#             'full_name': request.POST['full_name'],
#             'email': request.POST['email'],
#             'phone_number': request.POST['phone_number'],
#             'country': request.POST['country'],
#             'postcode': request.POST['postcode'],
#             'town_or_city': request.POST['town_or_city'],
#             'street_address1': request.POST['street_address1'],
#             'street_address2': request.POST['street_address2'],
#             'county': request.POST['county'],
#         }
#         order_form = OrderForm(form_data)
#         if order_form.is_valid():
#             order = order_form.save()

#         for product_id, quantity in cart.items():
#             product = get_object_or_404(Product, pk=product_id)
#             total += quantity * product.price
#             product_count += quantity
#             cart_items.append({
#                 'product_id': product_id,
#                 'quantity': quantity,
#                 'product': product,
#             })
#             cart_items.save()
#         return redirect(reverse('checkout_approved', args=[order.cart_items]))

#     cart = request.session.get('cart', {})
#     if not cart:
#         messages.error(request, "There's nothing in your bag at the moment")
#         return redirect(reverse('products'))

#     current_cart = cart_contents(request)
#     total = current_cart['grand_total']
#     stripe_total = round(total * 100)
#     stripe.api_key = stripe_secret_key
#     intent = stripe.PaymentIntent.create(
#         amount=stripe_total,
#         currency=settings.STRIPE_CURRENCY,
#     )

#     print(intent)

#     order_form = OrderForm()

#     if not stripe_public_key:
#         messages.warning(request, 'Stripe public key is missing. \
#             Did you forget to set it in your environment?')

#     template = 'checkout/checkout.html'
#     context = {
#         'order_form': order_form,
#         'stripe_public_key': stripe_public_key,
#         'client_secret': intent.client_secret,
#     }
#     cart = request.session.get('cart', {})

#     return render(request, template, context)


# def checkout_approved(request, cart_items):

#     order = get_object_or_404(Order, cart_items=cart_items)
#     messages.success(request, f'Order successfully processed!')

#     if 'cart' in request.session:
#         del request.session['cart']

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#     }

#     return render(request, template, context)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret')
            order.stripe_pid = pid
            order.original_bag = json.dumps(cart)
            order.save()
            for product_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        # if request.user.is_authenticated:
        #     try:
        #         profile = UserProfile.objects.get(user=request.user)
        #         order_form = OrderForm(initial={
        #             'full_name': profile.user.get_full_name(),
        #             'email': profile.user.email,
        #             'phone_number': profile.default_phone_number,
        #             'country': profile.default_country,
        #             'postcode': profile.default_postcode,
        #             'town_or_city': profile.default_town_or_city,
        #             'street_address1': profile.default_street_address1,
        #             'street_address2': profile.default_street_address2,
        #             'county': profile.default_county,
        #         })
        #     except UserProfile.DoesNotExist:
        #         order_form = OrderForm()
        # else:
        #     order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


    from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm, Order
from products.models import Product
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
            })
            cart_items.save()
        return redirect(reverse('checkout_approved', args=[order.cart_items]))

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    cart = request.session.get('cart', {})

    return render(request, template, context)


def checkout_approved(request, cart_items):

    order = get_object_or_404(Order, cart_items=cart_items)
    messages.success(request, f'Order successfully processed!')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)