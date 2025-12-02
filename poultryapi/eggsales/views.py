from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Eggsales
from .serializers import EggsalesSerializer


class EggsalesListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/eggsales/      -> list all eggsales (with optional filters)   
    POST /api/eggsales/      -> create a new eggsales
    """
    queryset = Eggsales.objects.all()          
    serializer_class = EggsalesSerializer         
     
    def get_queryset(self):    
        queryset = Eggsales.objects.all()
   
        # Optional filters via query parameters
        flock = self.request.query_params.get("flock")   
        payment_method = self.request.query_params.get("payment_method")  

        if flock:
            queryset = queryset.filter(flock__icontains=flock)   

        if payment_method:       
            queryset = queryset.filter(payment_method__icontains=payment_method)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = EggsalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Eggsales created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EggsalesCountView(generics.GenericAPIView):
    """   
    GET /api/eggsales/count/        
    GET /api/eggsales/count/?flock=                  
    GET /api/eggsales/count/?payment_method=
    """   
    queryset = Eggsales.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Eggsales.objects.all()

        flock = request.query_params.get("flock")            
        payment_method = request.query_params.get("payment_method")
         
        if flock:
            queryset = queryset.filter(flock__icontains=flock)  

        if payment_method:    
            queryset = queryset.filter(payment_method__icontains=payment_method)


        return Response({"count": queryset.count()})
