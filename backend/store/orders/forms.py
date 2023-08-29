from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Order.authorUser = request.user.username TODO доделать привязку автора

    class Meta:
        model = Order
        fields = [
            'country',
            'city',
            'postal_code',
            'address',
            'name',
            'email',
            'phone',
            'delivery'
        ]

        widgets = {
            'country': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Страна',
                }
            ),

            'city': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Город',
                }
            ),

            'postal_code': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Индекс',
                }
            ),

            'address': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Адресс',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'ФИО',
                }
            ),

            'email': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Email',
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Телефон',
                }
            ),

            'delivery': forms.RadioSelect

        }

        # country = forms.CharField(
        #     label='Страна',
        #     widget=forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
        #             "placeholder": 'Страна',
        #         }
        #     )
        # )

        # DELIVERY = [
        #     ('Почтой России', 'Почтой России'),
        #     ('Транспортной компанией', 'Транспортной компанией'),
        #     ('Самовывоз', 'Самовывоз'),
        # ]
        #
        # delivery = forms.MultipleChoiceField(
        #     required=False,
        #     widget=forms.CheckboxSelectMultiple,
        #     choices=DELIVERY,
        # )

class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]