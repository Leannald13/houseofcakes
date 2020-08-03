from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from.models import Contact

# Created an env var for the admin email so not in code.
ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:

            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email'],
            )

            form.save()

        else:
            form = Contact(
                contact_title=request.POST['contact_title'],
                contact_body=request.POST['contact_body'],
                email=request.POST['email']
            )

            form.save()

        messages.success(request, 'Your enquiry has been submitted, we will get back to you shortly.')
        return redirect('home')

    else:
        if request.user.is_authenticated:
            form = ContactForm(
                initial={'email': request.user.email}
            )
        else:
            form = ContactForm()

    context = {
        'contact': 'active',
        'form': form
    }

    return render(request, 'contact/contact.html', context)
