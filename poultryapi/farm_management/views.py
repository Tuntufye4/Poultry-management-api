from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import FarmManagement
from .serializers import FarmManagementSerializer             

    
class FarmManagementView(generics.ListCreateAPIView):   
    """      
    GET  /api/expenses/      -> list all expenses (with optional filters)      
    POST /api/expenses/      -> create a new expense 
    """
    queryset = FarmManagement.objects.all()
    serializer_class = FarmManagementSerializer
     
    def get_queryset(self):
        queryset = FarmManagement.objects.all()  

        # Optional filters via query parameters
        activity = self.request.query_params.get("activity")   

        if activity:
            queryset = queryset.filter(activity__icontains=activity)           

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = FarmManagementSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()   
            return Response(
                {"message": "Farm management details created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmManagementCountView(generics.GenericAPIView):
    """
    GET /api/expenses/count/        -> total expenses
    GET /api/expenses/count/?expense_type=
    GET /api/expenses/count/?flock=
    GET /api/expenses/count/?payment_method=

    """   
    queryset = FarmManagement.objects.all()    

    def get(self, request, *args, **kwargs):     
        queryset = FarmManagement.objects.all()

        activity = request.query_params.get("activity")

        if activity:
            queryset = queryset.filter(activity__icontains=activity)
       

        return Response({"count": queryset.count()})
       