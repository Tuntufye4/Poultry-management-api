from rest_framework import serializers
from .models import SalesManagement    

class SalesManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesManagement 
        fields = '__all__'          