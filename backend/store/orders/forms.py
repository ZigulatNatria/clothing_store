from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Order.authorUser = request.user.username TODO доделать привязку автора
    country = forms.CharField(
        label='Страна',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Страна',
            }
        )
    )

    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Город',
            }
        )
    )

    postal_code = forms.CharField(
        label='Индекс',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Индекс',
            }
        )
    )

    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Адрес',
            }
        )
    )

    name = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'ФИО',
            }
        )
    )

    email = forms.CharField(
        label='Эл.почта',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Email',

            }
        )
    )

    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
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