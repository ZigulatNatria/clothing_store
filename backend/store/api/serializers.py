from rest_framework import serializers
from shop.models import Product, Collection, CategoryProduct, ClothingCategories, \
    ClientCategory, Stock


class ProductSerializer(serializers.ModelSerializer):
    # Вывод имени полей ForeignKey
    collection = serializers.SlugRelatedField(slug_field='name', read_only=True)
    stock_availability = serializers.SlugRelatedField(slug_field='quantity', read_only=True)
    category_product = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('__all__')


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('__all__')


class CategoryProductSerializer(serializers.ModelSerializer):
    client_category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CategoryProduct
        fields = ('__all__')


class ClothingCategoriesSerializer(serializers.ModelSerializer):
    client_category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ClothingCategories
        fields = ('__all__')


class ClientCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientCategory
        fields = ('__all__')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('__all__')