from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Nutrition
from .serializers import NutritionSerializer

   
class NutritionListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/nutritionworkflow/      -> list all flocks (with optional filters)   
    POST /api/nutritionworkflow/      -> create a new nutrition workflow   
    """
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer
     
    def get_queryset(self):
        queryset = Nutrition.objects.all()   

        # Optional filters via query parameters
        feed_type = self.request.query_params.get("feed_type")
        feed_brand = self.request.query_params.get("feed_brand")   
        flock = self.request.query_params.get("flock") 

        if feed_type:
            queryset = queryset.filter(feed_type__icontains=feed_type)

        if feed_brand:
            queryset = queryset.filter(feed_brand__icontains=feed_brand)   

        if flock:
            queryset = queryset.filter(flock__icontains=flock)   

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = NutritionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Nutrition workflow created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutritionCountView(generics.GenericAPIView):
    """
    GET /api/nutritionworkflow/count/             
    GET /api/nutritionworkflow/count/?feed_type=
    GET /api/nutritionworkflow/count/?feed_brand=      
    """
    queryset = Nutrition.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Nutrition.objects.all()

        feed_type = request.query_params.get("feed_type")
        feed_brand = request.query_params.get("feed_brand")
        flock = request.query_params.get("flock")

        if feed_type:
            queryset = queryset.filter(feed_type__icontains=feed_type)

        if feed_brand:
            queryset = queryset.filter(feed_brand__icontains=feed_brand)

        if flock:   
            queryset = queryset.filter(flock__icontains=flock)

        return Response({"count": queryset.count()})
