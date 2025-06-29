from rest_framework import serializers
from inventory.models import locations

class PublicLocationSerializer(serializers.ModelSerializer):
    location_type_display = serializers.CharField(source='get_loaction_type_display',read_only=True)
    class Meta:
        model = locations
        fields = ['id','name','location_type_display','address','postal_code']
class AdminLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = locations
        fields = '__all__'