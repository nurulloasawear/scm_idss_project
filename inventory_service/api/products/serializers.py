from rest_framework import serializers
from inventory.models import products

class PublicProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = products
        fields = ['id','sku','name','description','category_name']
class AdminProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = products
        fields = "__all__"
        extra_kwargs = {
            'category':{'write_only':True,'required':False,'allow_null':True}
        }