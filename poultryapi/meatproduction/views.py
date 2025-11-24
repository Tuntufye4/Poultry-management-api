from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count
    
from .models import Meatproduction
from .serializers import MeatproductionSerializer

   
class MeatproductionListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/meatproduction/      -> list all meat production (with optional filters)   
    POST /api/meatproduction/      -> create a new meat production list   
    """    
    queryset = Meatproduction.objects.all()    
    serializer_class = MeatproductionSerializer      
         
    def get_queryset(self):
        queryset = Meatproduction.objects.all()   

        # Optional filters via query parameters
        flock = self.request.query_params.get("flock")  

        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = MeatproductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Meat production created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeatproductionCountView(generics.GenericAPIView):
    """
    GET /api/meatproduction/count/        -> total treatments  
    GET /api/meatproduction/count/?treatment_type       
    """   
    queryset = Meatproduction.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Meatproduction.objects.all()    

        flock = request.query_params.get("flock")  
     
        if flock:
            queryset = queryset.filter(flock__icontains=flock)   

        return Response({"count": queryset.count()})
