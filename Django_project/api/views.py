from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from mainapp.models import Product
from .paginations import StandartPagination
from .serializers import ProductSerializer


class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['name', 'category']
    search_fields = ['name', 'price']
    pagination_class = StandartPagination

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

