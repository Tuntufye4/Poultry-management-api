from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count
   
from .models import Meatsales   
from .serializers import MeatsalesSerializer    


class MeatsalesListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/meatsales/      -> list all meatsales (with optional filters)     
    POST /api/meatsales/      -> create a new meatsales list
    """
    queryset = Meatsales.objects.all()          
    serializer_class = MeatsalesSerializer          
     
    def get_queryset(self):    
        queryset = Meatsales.objects.all()
   
        # Optional filters via query parameters  
        flock = self.request.query_params.get("flock")
        payment_method = self.request.query_params.get("payment_method") 
        chicken_type = self.request.query_params.get("chicken_type") 
        processing_type = self.request.query_params.get("processing_type")

        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        if payment_method:       
            queryset = queryset.filter(payment_method__icontains=payment_method)  

        if chicken_type:
            queryset = queryset.filter(chicken_type__icontains=chicken_type)

        if processing_type:
            queryset = queryset.filter(processing_type__icontains=processing_type)

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = MeatsalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Meatsales created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeatsalesCountView(generics.GenericAPIView):
    """   
    GET /api/meatsales/count/  
    GET /api/meatsales/count/?flock=      
    GET /api/meatsales/count/?payment_method=
    GET /api/meatsales/count/?chicken_type=
    GET /api/meatsales/count/?processing_type=   
 
    """   
    queryset = Meatsales.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Meatsales.objects.all()
        
        flock = request.query_params.get("flock")
        payment_method = request.query_params.get("payment_method") 
        chicken_type = request.query_params.get("chicken_type")
        processing_type = request.query_params.get("processing_type")
        
        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        if payment_method:    
            queryset = queryset.filter(payment_method__icontains=payment_method)

        if chicken_type:
            queryset = queryset.filter(chicken_type__icontains=chicken_type)

        if processing_type:
            queryset = queryset.filter(processing_type__icontains=processing_type)


        return Response({"count": queryset.count()})
    