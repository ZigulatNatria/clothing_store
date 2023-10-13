from django import forms
from shop.models import Product, Size


class CartAddProductForm(forms.Form):

    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]

    # colors = Color.objects.all()
    # color_list = []
    # for col in colors:
    #     color_list.append(col.name_color)
    # PRODUCT_COLOR_CHOICES = [(str(k), str(k)) for k in color_list]

    sizes = Size.objects.all()
    size_list = []
    for size in sizes:
        size_list.append(size.size)
    PRODUCT_SIZE_CHOICES = [(str(s), str(s)) for s in size_list]

    quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # color = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_COLOR_CHOICES, coerce=str)
    size = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_SIZE_CHOICES, coerce=str)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)