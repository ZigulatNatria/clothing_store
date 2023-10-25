from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

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
            # 'delivery',           #TODO добавить или оставить
            # 'type_pay'            #TODO добавить или оставить
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

            # 'email': forms.TextInput(
            #     attrs={
            #         "class": "form-control",
            #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
            #         "placeholder": 'Email',
            #     }
            # ),
            #
            # 'phone': forms.TextInput(
            #     attrs={
            #         "class": "form-control",
            #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
            #         "placeholder": 'Телефон',
            #     }
            # ),

            'delivery': forms.RadioSelect,

            'type_pay': forms.RadioSelect

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

        # CHOICES_PAY = [
        #     ('Оплата картой онилайн', 'Оплата картой онилайн'),
        # ]
        #
        # type_pay = forms.MultipleChoiceField(
        #     required=False,
        #     # widget=forms.CheckboxSelectMultiple,
        #     widget=forms.RadioSelect,
        #     choices=CHOICES_PAY,
        # )


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]