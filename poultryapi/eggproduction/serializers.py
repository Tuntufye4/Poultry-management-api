from rest_framework import serializers
from .models import Eggproduction   

class EggproductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eggproduction      
        fields = '__all__'        