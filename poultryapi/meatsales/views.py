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
        payment_method = self.request.query_params.get("payment_method")  

        if payment_method:       
            queryset = queryset.filter(payment_method__icontains=payment_method)  

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
    GET /api/meatsales/count/?payment_method=
 
    """   
    queryset = Meatsales.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Meatsales.objects.all()

        payment_method = request.query_params.get("payment_method")  

        if payment_method:    
            queryset = queryset.filter(payment_method__icontains=payment_method)


        return Response({"count": queryset.count()})
