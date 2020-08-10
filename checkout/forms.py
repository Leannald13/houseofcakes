from django import forms
from .models import Order
import datetime


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class MakePaymentForm(forms.Form):
    """
    Create form for payments via stripe
    """

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(
        min_length=16,
        max_length=16,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Credit Card Number'
        })
    )

    cvv = forms.CharField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVV',
            'required': 'True',
        })
    )

    expiry_month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    expiry_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        required=False,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    stripe_id = forms.CharField(
        widget=forms.HiddenInput
    )
