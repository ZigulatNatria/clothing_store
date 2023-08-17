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

    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    postal_code = forms.CharField(
        label='Индекс',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    name = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    email = forms.CharField(
        label='Эл.почта',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    phone = forms.CharField(
        label='Телефон',
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