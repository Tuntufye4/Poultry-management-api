from rest_framework import serializers
from .models import Eggsales   

class EggsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eggsales     
        fields = '__all__'            