from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Inventory
from .serializers import InventorySerializer


class InventoryListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/inventory/      -> list all inventory (with optional filters)   
    POST /api/inventory/      -> create a new inventory list
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
     
    def get_queryset(self):
        queryset = Inventory.objects.all()
   
        # Optional filters via query parameters
        category = self.request.query_params.get("category")
        supplier = self.request.query_params.get("supplier") 
        source_supplier = self.request_params.get("source_supplier") 
        item_name = self.request_params.get("item_name")     
     
        if category:
            queryset = queryset.filter(category__icontains=category)

        if supplier:   
            queryset = queryset.filter(supplier__icontains=supplier)  

        if source_supplier:
            queryset = queryset.filter(source_supplier__icontains=source_supplier) 
            
        if item_name:
            queryset = queryset.filter(item_name__icontains=item_name)

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Inventory created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryCountView(generics.GenericAPIView):
    """
    GET /api/inventory/count/        -> total 
    GET /api/inventory/count/?category=
    """
    queryset = Inventory.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Inventory.objects.all()

        category = request.query_params.get("category")   
        supplier = request.query_params.get("supplier")
        source_supplier = request.query_params.get("source_supplier")
        item_name = request.query_params.get("item_name")

        if category:   
            queryset = queryset.filter(category__icontains=category)

        if supplier:
            queryset = queryset.filter(supplier__icontains=supplier)

        if source_supplier:
            queryset = queryset.filter(source_supplier__icontains=source_supplier)

        if item_name:
            queryset = queryset.filter(item_name__icontains=item_name)

        return Response({"count": queryset.count()})
     