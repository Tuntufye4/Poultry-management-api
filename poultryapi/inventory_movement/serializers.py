from rest_framework import serializers
from .models import Inventory_movement  

class InventorymovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_movement  
        fields = '__all__'                       