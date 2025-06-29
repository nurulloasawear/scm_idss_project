from rest_framework import serializers
from inventory.models import category

class PubluicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
        