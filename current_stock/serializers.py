from rest_framework import serializers
from .models import Currentstock   

class CurrentStockSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Currentstock     
        fields = '__all__'            