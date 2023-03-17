from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, CollectionSerializer, CategoryProductSerializer, \
    ClothingCategoriesSerializer, ClientCategorySerializer
from shop.models import Product, Collection, CategoryProduct, ClothingCategories, ClientCategory

# Create your views here.
class ProductAPIVew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CollectionAPIVew(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CategoryProductAPIVew(generics.ListAPIView):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer


class ClothingCategoriesAPIVew(generics.ListAPIView):
    queryset = ClothingCategories.objects.all()
    serializer_class = ClothingCategoriesSerializer


class ClientCategoryAPIVew(generics.ListAPIView):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer