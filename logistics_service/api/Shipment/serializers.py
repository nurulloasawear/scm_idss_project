from rest_framework import serializers
from logistics.models import Carrier, Shipment 

class PublicShipmentSerializer(serializers.ModelSerializer):
    carrier_name = serializers.CharField(source='carrier.name', read_only=True, default='N/A')
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Shipment
        fields = ['id', 'customer_order_id', 'carrier_name', 'tracking_number', 'status_display', 'estimated_delivery_at']

class AdminShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'