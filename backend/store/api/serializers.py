from rest_framework import serializers
from shop.models import Product, Collection, CategoryProduct, ClothingCategories, ClientCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('__all__')


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ('__all__')


class ClothingCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCategories
        fields = ('__all__')


class ClientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = ('__all__')