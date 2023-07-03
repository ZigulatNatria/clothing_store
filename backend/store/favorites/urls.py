from django.urls import path
from .views import favorites_detail, favorites_add, favorites_remove

urlpatterns =[
    path('', favorites_detail, name='favorites_detail'),
    path('favorites_add/<int:product_id>/', favorites_add, name='favorites_add'),
    path('remove/<int:product_id>/', favorites_remove, name='favorites_remove'),
]