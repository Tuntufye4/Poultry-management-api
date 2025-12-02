from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Culling
from .serializers import CullingSerializer

    
class CullingListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/culling/      -> list all flocks (with optional filters)   
    POST /api/culling/      -> create a new flock    
    """
    queryset = Culling.objects.all()        
    serializer_class = CullingSerializer    
     
    def get_queryset(self):    
        queryset = Culling.objects.all()
   
        # Optional filters via query parameters    
        flock = self.request.query_params.get("flock")
        payment_method = self.request.query_params.get("payment_method")   
      
        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        if payment_method:   
            queryset = queryset.filter(payment_method__icontains=payment_method)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = CullingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Culling created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CullingCountView(generics.GenericAPIView):
    """
    GET /api/culling/count/        -> total flocks
    GET /api/culling/count/?flock=
    GET /api/culling/count/?payment_method=
    """
    queryset = Culling.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Culling.objects.all()

        flock = request.query_params.get("flock")
        payment_method = request.query_params.get("payment_method")
         
        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        if payment_method:    
            queryset = queryset.filter(payment_method__icontains=payment_method)
   

        return Response({"count": queryset.count()})
