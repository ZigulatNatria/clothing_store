from django import forms
from shop.models import Color, Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
# PRODUCT_COLOR_CHOICES = Color.name_color
PRODUCT_COLOR_CHOICES = [
    ('Красный', 'Красный'),
    ('Белый', 'Белый'),
    ('Чёрный', 'Чёрный'),
    ('Зелёный', 'Зелёный')
]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    color = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_COLOR_CHOICES, coerce=str)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)