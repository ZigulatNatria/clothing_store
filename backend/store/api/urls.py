from django.urls import path
from .views import ProductAPIVew


urlpatterns =[
    path('products/', ProductAPIVew.as_view()),
]