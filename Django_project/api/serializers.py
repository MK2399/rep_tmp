from rest_framework.serializers import ModelSerializer

from mainapp.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'company', 'price')
