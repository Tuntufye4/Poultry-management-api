from rest_framework import serializers
from .models import Flocksetup    

class FlocksetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flocksetup
        fields = '__all__'    