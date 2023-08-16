from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Order.authorUser = request.user.username TODO доделать привязку автора
    country = forms.CharField(
        label='Страна',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Order
        fields = [
            # 'country',
            'city',
            'postal_code',
            'address',
            'name',
            'email',
            'phone',
        ]


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]