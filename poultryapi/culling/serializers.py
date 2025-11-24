from rest_framework import serializers
from .models import Culling    

class CullingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culling
        fields = '__all__'          