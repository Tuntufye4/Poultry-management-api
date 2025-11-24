from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count
    
from .models import Sales
from .serializers import SalesSerializer

   
class SalesListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/sales/      -> list all sales (with optional filters)   
    POST /api/sales/      -> create a new sale
    """    
    queryset = Sales.objects.all()    
    serializer_class = SalesSerializer   
     
    def get_queryset(self):
        queryset = Sales.objects.all()

        # Optional filters via query parameters
        flock = self.request.query_params.get("flock")
        trays_sold = self.request.query_params.get("trays_sold") 
        payment_method = self.request.query_params.get("payment_method")   

        if flock:
            queryset = queryset.filter(flock__icontains=flock)
 
        if trays_sold:    
            queryset = queryset.filter(trays_sold__icontains=trays_sold) 

        if payment_method:
            queryset = queryset.filter(payment_method__icontains=payment_method)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Sales created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesCountView(generics.GenericAPIView):
    """
    GET /api/sales/count/        -> total trays_sold  
    GET /api/sales/count/?trays_sold
    """
    queryset = Sales.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Sales.objects.all()    

        flock = request.query_params.get("flock")
        trays_sold = request.query_params.get("trays_sold")   
        payment_method = request.query_params.get("payment_method")
     
        if flock:
            queryset = queryset.filter(flock__icontains=flock)

        if trays_sold:
            queryset = queryset.filter(trays_sold__icontains=trays_sold)

        if payment_method:
            queryset = queryset.filter(payment_method__icontains=payment_method)

        return Response({"count": queryset.count()})
