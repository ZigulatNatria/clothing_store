from django.urls import path
from .views import ProductAPIVew, CollectionAPIVew, CategoryProductAPIVew, ClothingCategoriesAPIVew, \
    ClientCategoryAPIVew, StockAPIVew, ProductDetailAPIVew, CreateClientCategoryAPIVew, CreateCollectionAPIVew, \
    CreateClothingCategoriesAPIVew, CreateProductAPIVew, CreateStockAPIVew, CreateCategoryProductAPIVew


urlpatterns =[
    path('products/', ProductAPIVew.as_view()),
    path('collection/', CollectionAPIVew.as_view()),
    path('category_product/', CategoryProductAPIVew.as_view()),
    path('clothing_categories/', ClothingCategoriesAPIVew.as_view()),
    path('client_category/', ClientCategoryAPIVew.as_view()),
    path('stock/', StockAPIVew.as_view()),
    path('products/<int:pk>/', ProductDetailAPIVew.as_view()),
    #API для добавления
    path('add_client_category', CreateClientCategoryAPIVew.as_view()),
    path('add_collection', CreateCollectionAPIVew.as_view()),
    path('add_clothing_categories', CreateClothingCategoriesAPIVew.as_view()),
    path('add_product', CreateProductAPIVew.as_view()),
    path('add_stock', CreateStockAPIVew.as_view()),
    path('add_category_product', CreateCategoryProductAPIVew.as_view()),
]