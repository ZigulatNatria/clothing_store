from django.urls import path
from .views import IndexView, ProtectView

urlpatterns = [
    path('', IndexView.as_view()),
    path('my_info', ProtectView.as_view(), name='my_info'),
]