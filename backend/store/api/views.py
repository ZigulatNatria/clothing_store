from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CollectionSerializer, CategoryProductSerializer, \
    ClothingCategoriesSerializer, ClientCategorySerializer, StockSerializer
from shop.models import Product, Collection, CategoryProduct, ClothingCategories, \
    ClientCategory, Stock

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


class StockAPIVew(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

""" Вывод одного объекта Product из базы данных """
class ProductDetailAPIVew(APIView):

    def get(self, request, pk):                  # В get передаём параметры pk - это id выбранной модели
        product = Product.objects.get(id=pk)     # забираем нужный объект
        serializer = ProductSerializer(product)  # передаём его для серализации
        return Response(serializer.data)         # возвращаем в ответ сериализованные данные


class CreateProductAPIVew(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateCollectionAPIVew(APIView):

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateCategoryProductAPIVew(APIView):

    def post(self, request):
        serializer = CategoryProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateClothingCategoriesAPIVew(APIView):

    def post(self, request):
        serializer = ClothingCategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateClientCategoryAPIVew(APIView):

    def post(self, request):
        serializer = ClientCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateStockAPIVew(APIView):

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)