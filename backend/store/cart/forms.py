from django import forms
from shop.models import Product, Size


class CartAddProductForm(forms.Form):

    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]

    sizes = Size.objects.all()
    size_list = []
    for size in sizes:
        size_list.append(size.size)
    PRODUCT_SIZE_CHOICES = [(str(s), str(s)) for s in size_list]

    quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    size = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_SIZE_CHOICES, coerce=str)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)