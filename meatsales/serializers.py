from rest_framework import serializers
from .models import Meatsales   

class MeatsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meatsales     
        fields = '__all__'            