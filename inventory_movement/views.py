from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Inventory_movement
from .serializers import InventorymovementSerializer


class InventorymovementListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/inventory_movement/      -> list all inventory_movement (with optional filters)   
    POST /api/inventory_movement/      -> create a new inventory_movement list
    """
    queryset = Inventory_movement.objects.all()    
    serializer_class = InventorymovementSerializer            
     
    def get_queryset(self):
        queryset = Inventory_movement.objects.all()
   
        # Optional filters via query parameters
        inventory_item = self.request.query_params.get("inventory_item")
        movement_type = self.request.query_params.get("movement_type")   
     
        if inventory_item:
            queryset = queryset.filter(inventory_item__icontains=inventory_item)

        if movement_type:   
            queryset = queryset.filter(movement_type__icontains=movement_type)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = InventorymovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Inventory movement created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventorymovementCountView(generics.GenericAPIView):
    """
    GET /api/inventory_movement/count/        
    GET /api/inventory_movement/count/?inventory_item=
    """
    queryset = Inventory_movement.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Inventory_movement.objects.all()

        inventory_item = request.query_params.get("inventory_item")   
        movement_type = request.query_params.get("movement_type")

        if inventory_item:   
            queryset = queryset.filter(inventory_item__icontains=inventory_item)

        if movement_type:
            queryset = queryset.filter(movement_type__icontains=movement_type)


        return Response({"count": queryset.count()})
     