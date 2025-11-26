from rest_framework import serializers
from .models import LogisticsManagement    

class LogisticsManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticsManagement 
        fields = '__all__'             