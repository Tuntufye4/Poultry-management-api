from rest_framework import serializers
from .models import Manuresales   

class ManuresalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manuresales                            
        fields = '__all__'                  