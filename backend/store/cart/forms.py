from django import forms
from shop.models import Color, Product, Size
from shop.views import ProductDetail

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

PRODUCT_SIZE_CHOICES = [
    ('50', '50'),
    ('60', '60'),
]

PRODUCT_COLOR_CHOICES = [
    ('Красный', 'Красный'),
    ('Жёлтый', 'Жёлтый')
]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    color = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_COLOR_CHOICES, coerce=str)
    size = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_SIZE_CHOICES, coerce=str)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)