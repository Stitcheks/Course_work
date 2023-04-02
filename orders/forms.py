from django import forms
from django.core.exceptions import ValidationError
from .models import Contact, Order


def phone_number_validator(phone_number):
    if phone_number.startswith('+375') and (phone_number[4:6] in ['25', '29', '33', '44']):
        return phone_number
    else:
        raise ValidationError('Неправильный номер телефона')


class ContactModelForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=13, validators=[phone_number_validator])

    class Meta:
        model = Contact
        fields = ('name', 'phone_number',)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number']

