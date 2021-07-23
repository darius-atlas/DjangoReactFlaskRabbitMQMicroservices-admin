form rest_framework import serializsers
from .models import Product


class ProductSerializer(serializsers.ModelSerializer):
    class Meta:
        model = Product
        filds = '__all__'