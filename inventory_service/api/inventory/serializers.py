from rest_framework import serializers
from inventory.models  import inventory

class PublicInventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    class Meta:
        model = inventory
        fields = ['id', 'product_name', 'location_name', 'quantity']

class AdminInventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    class Meta:
        model = inventory
        fields = '__all__'
        extra_kwargs = {
            'product': {'write_only': True},
            'location': {'write_only': True},
        }
