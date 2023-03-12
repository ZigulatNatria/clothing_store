from django.urls import path
from .views import CategoryProductListView, ProductDetail, product_categories


urlpatterns =[
    # path('products/<int:pk>/', ProductsListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('products/<int:category_product_id>/', product_categories, name='products'),
    path('categories/', CategoryProductListView.as_view(), name='categories'),
]