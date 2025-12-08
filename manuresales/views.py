from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Manuresales   
from .serializers import ManuresalesSerializer    


class ManuresalesListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/manuresales/      -> list all manuresales (with optional filters)   
    POST /api/manuresales/      -> create a new manuresales list
    """
    queryset = Manuresales.objects.all()          
    serializer_class = ManuresalesSerializer          
     
    def get_queryset(self):    
        queryset = Manuresales.objects.all()
   
        # Optional filters via query parameters  
        payment_method = self.request.query_params.get("payment_method") 
        manure_type = self.request.query_params.get("manure_type")         
        manure_quality = self.request.query_params.get("manure_quality")

        if payment_method:       
            queryset = queryset.filter(payment_method__icontains=payment_method)  

        if manure_type:
            queryset = queryset.filter(manure_type__icontains=manure_type)

        if manure_quality:
            queryset = queryset.filter(manure_quality__icontains=manure_quality)

        return queryset    

    def post(self, request, *args, **kwargs):
        serializer = ManuresalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Manuresales created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManuresalesCountView(generics.GenericAPIView):
    """   
    GET /api/manuresales/count/        
    GET /api/manuresales/count/?payment_method=
    GET /api/manuresales/count/?manure_type=
    GET /api/manuresales/count/?manure_quality=   
    """   
    queryset = Manuresales.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Manuresales.objects.all()

        payment_method = request.query_params.get("payment_method")  
        manure_type = request.query_params.get("manure_type")    
        manure_quality = request.query_params.get("manure_quality")

        if payment_method:    
            queryset = queryset.filter(payment_method__icontains=payment_method)

        if manure_type:
            queryset = queryset.filter(manure_type__icontains=manure_type)

        if manure_quality:
            queryset = queryset.filter(manure_quality__icontains=manure_quality)


        return Response({"count": queryset.count()})
