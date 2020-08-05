from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
import os
from .forms import ContactForm
from.models import Contact


def contact(request):
    if request.method == 'POST':

        form = Contact(
            contact_title=request.POST['contact_title'],
            contact_body=request.POST['contact_body'],
            email=request.POST['email'],
        )

        form.save()
        return redirect('home')

        send_mail(
            request.POST['email'],
            request.POST['contact_body'],
            'House of Cakes',
            ['leannald13@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect('/contact/contact/')


