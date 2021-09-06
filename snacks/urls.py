from django.urls import path
from .views import SnacksDetail, SnacksList

urlpatterns = [
    path('', SnacksList.as_view(), name='snacks_list'),
    path('<int:pk>/', SnacksDetail.as_view(), name='snacks_detail'),
]