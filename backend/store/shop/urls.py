from django.urls import path
from .views import ProductsListView, CategoryProductListView


urlpatterns =[
    path('products/', ProductsListView.as_view(), name='products'),
    path('categories/', CategoryProductListView.as_view(), name='categories'),
]