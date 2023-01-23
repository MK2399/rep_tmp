from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import ProductsList
from api.views import ProductDetail

urlpatterns = [
    path('product_api/', ProductsList.as_view()),
    path('product_api/<int:pk>/', ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
