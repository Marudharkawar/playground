from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'

    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else None

    def get_updated_by(self, obj):
        return obj.updated_by.username if obj.updated_by else None
