from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from shop.models import Product

# Create your views here.
class ProductAPIVew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer