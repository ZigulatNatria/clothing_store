from django.urls import path
from .views import category_product_list_view, ProductDetail, product_categories, \
    ClothingCategoriesView, FirstPage, search, user_follow, add_subscribe, delete_subscribe, \
    add_favorite, delete_favorite, pay_info, delivery_info, return_info, contacts_info, NewsDetail, NewsList, \
    favorite_list, add_favorite_in_list, delete_favorite_in_list
from .pay import Pay


urlpatterns =[
    # path('products/<int:pk>/', ProductsListView.as_view(), name='products'),
    path('product/follow/', user_follow, name='user_follow'),
    path('product/sub/', add_subscribe, name='add_subscribe'),
    path('product/delete_favor/', delete_subscribe, name='delete_subscribe'),
    path('product/favorite/', favorite_list, name='favorite'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('products/<int:category_product_id>/', product_categories, name='products'),
    path('categories_global/<int:category_clothing_id>/', category_product_list_view, name='category_clothing'),
    # path('categories/', CategoryProductListView.as_view(), name='categories'),
    path('', FirstPage.as_view(), name='categories_global'),
    path('search/', search, name='search'),
    path('pay/', Pay.as_view(), name='pay'),
    #вкладки меню
    path('product/pay_info/', pay_info, name='pay_info'),
    path('product/delivery_info/', delivery_info, name='delivery_info'),
    path('product/return_info/', return_info, name='return_info'),
    path('product/contacts_info/', contacts_info, name='contacts_info'),
    #новости
    path('product/news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('product/news_list/', NewsList.as_view(), name='news_list'),
    #добавление и удаление из избранного
    path('product/add_favorite/', add_favorite, name='add_favorite'),
    path('product/add_favorite_list/', add_favorite_in_list, name='add_favorite_in_list'),
    path('product/delete_favorite/', delete_favorite, name='delete_favorite'),
    path('product/delete_favorite_list/', delete_favorite_in_list, name='delete_favorite_in_list'),
]