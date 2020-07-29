from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_approved/<cart_items>', views.checkout_approved, name='checkout_approved'),

]