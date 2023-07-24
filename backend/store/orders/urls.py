from django.urls import path
from .views import order_create, OrderList, OrderUpdate, OrderDetail


app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('order_list/', OrderList.as_view(), name='order_list'),
    path('order_update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('order_detail/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
]