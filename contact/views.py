from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from.models import Contact


def contact(request):
    """ Contact form for users to send message """
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

        send_mail(
            request.POST['email'],
            request.POST['contact_body'],
            'House of Cakes',
            ['leannald13@gmail.com'],
            fail_silently=False,
        )

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
