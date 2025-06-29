from rest_framework import serializers
from logistics.models import Carrier, Shipment

class PublicCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'service_type']

class AdminCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'

