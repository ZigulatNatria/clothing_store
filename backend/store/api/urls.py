from django.urls import path
from .views import ProductAPIVew, CollectionAPIVew, CategoryProductAPIVew, ClothingCategoriesAPIVew, \
    ClientCategoryAPIVew, StockAPIVew, ProductDetailAPIVew


urlpatterns =[
    path('products/', ProductAPIVew.as_view()),
    path('collection/', CollectionAPIVew.as_view()),
    path('category_product/', CategoryProductAPIVew.as_view()),
    path('category_product/', CategoryProductAPIVew.as_view()),
    path('clothing_categories/', ClothingCategoriesAPIVew.as_view()),
    path('client_category/', ClientCategoryAPIVew.as_view()),
    path('stock/', StockAPIVew.as_view()),
    path('products/<int:pk>/', ProductDetailAPIVew.as_view()),
]