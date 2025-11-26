from rest_framework import serializers
from .models import FarmManagement    

class FarmManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmManagement 
        fields = '__all__'          