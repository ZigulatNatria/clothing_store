from django import forms
from django_filters import FilterSet, CharFilter, ChoiceFilter, MultipleChoiceFilter, \
    ModelChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Product, Color, Size


class ProductFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    colors = ModelChoiceFilter(
        label='Цвет',
        queryset=Color.objects.all(),
        field_name='colors',
        widget=forms.Select(
            attrs={
                # "class": "form-control text-white text-center",
                "class": "form-select",
            }
        )
    )

    size = ModelChoiceFilter(
        label='Размер',
        queryset=Size.objects.all(),
        field_name='size',
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )

    class Meta:
        model = Product
        fields = (
           'size',
           'colors',
           # 'price',
        )  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
