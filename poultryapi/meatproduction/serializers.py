from rest_framework import serializers
from .models import Meatproduction   

class MeatproductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meatproduction      
        fields = '__all__'             