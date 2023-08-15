from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Order.authorUser = request.user.username TODO доделать привязку автора
    class Meta:
        model = Order
        fields = [
            'name',
            'email',
            'address',
            'postal_code',
            'city'
        ]


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]