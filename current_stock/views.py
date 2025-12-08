from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Currentstock      
from .serializers import CurrentStockSerializer
  

class CurrentStockListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/current_stock/      -> list all current stocks (with optional filters)   
    POST /api/current_stock/      -> create a new current stock
    """
    queryset = Currentstock.objects.all()          
    serializer_class = CurrentStockSerializer       
     
    def get_queryset(self):    
        queryset = Currentstock.objects.all()
   
        # Optional filters via query parameters
        manure_packaging_type = self.request.query_params.get("manure_packaging_type") 
        chicken_packaging_type = self.request.query_params.get("chicken_packaging_type")   

        if manure_packaging_type:
            queryset = queryset.filter(manure_packaging_type__icontains=manure_packaging_type)   

        if chicken_packaging_type:
            queryset = queryset.filter(chicken_packaging_type__icontains=chicken_packaging_type)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = CurrentStockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "current stock created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentStockCountView(generics.GenericAPIView):
    """   
    GET /api/current_stock/count/        
    GET /api/current_stock/count/?manure_packaging_type=    
    GET /api/current_stock/count/?chicken_packaging_type=                      
    """   
    queryset = Currentstock.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Currentstock.objects.all()

        manure_packaging_type = request.query_params.get("manure_packaging_type")            
        chicken_packaging_type = request.query_params.get("chicken_packaging_type")
         
        if manure_packaging_type:
            queryset = queryset.filter(manure_packaging_type__icontains=manure_packaging_type)  

        if chicken_packaging_type:
            queryset = queryset.filter(chicken_packaging_type__icontains=chicken_packaging_type) 


        return Response({"count": queryset.count()})
