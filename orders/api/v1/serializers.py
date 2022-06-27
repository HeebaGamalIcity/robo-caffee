from rest_framework import serializers
from orders.models import Product_order


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_order
        fields = ("order", "product", "topping")