from django.urls import path
from .views import category_product_list_view, ProductDetail, product_categories, \
    ClothingCategoriesView, FirstPage, FavoriteListView, search, user_follow, add_subscribe, delete_subscribe


urlpatterns =[
    # path('products/<int:pk>/', ProductsListView.as_view(), name='products'),
    path('product/follow/', user_follow, name='user_follow'),
    path('product/sub/', add_subscribe, name='add_subscribe'),
    path('product/delete_favor/', delete_subscribe, name='delete_subscribe'),
    path('product/favorite/', FavoriteListView.as_view(), name='favorite'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('products/<int:category_product_id>/', product_categories, name='products'),
    path('categories_global/<int:category_clothing_id>/', category_product_list_view, name='category_clothing'),
    # path('categories/', CategoryProductListView.as_view(), name='categories'),
    path('', FirstPage.as_view(), name='categories_global'),
    path('search/', search, name='search')
]