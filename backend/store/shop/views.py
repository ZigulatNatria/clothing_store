from django.shortcuts import render
from .models import Product, CategoryProduct
from django.views.generic import ListView

class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class CategoryProductListView(ListView):
    model = CategoryProduct
    template_name = 'categories.html'
    context_object_name = 'categories'
    queryset = CategoryProduct.objects.all()