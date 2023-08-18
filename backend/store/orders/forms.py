from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Order.authorUser = request.user.username TODO доделать привязку автора
    country = forms.CharField(
        label='Страна',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Страна',
            }
        )
    )

    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Город',
            }
        )
    )

    postal_code = forms.CharField(
        label='Индекс',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Индекс',
            }
        )
    )

    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Адрес',
            }
        )
    )

    name = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'ФИО',
            }
        )
    )

    email = forms.CharField(
        label='Эл.почта',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Email',

            }
        )
    )

    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                "placeholder": 'Телефон',
            }
        )
    )

    class Meta:
        model = Order
        fields = [
            # 'country',
            # 'city',
            # 'postal_code',
            # 'address',
            # 'name',
            # 'email',
            # 'phone',
        ]


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]