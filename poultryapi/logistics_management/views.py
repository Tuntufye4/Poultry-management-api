from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import LogisticsManagement
from .serializers import LogisticsManagementSerializer             

    
class LogisticsManagementView(generics.ListCreateAPIView):   
    """      
    GET  /api/expenses/      -> list all expenses (with optional filters)      
    POST /api/expenses/      -> create a new expense 
    """
    queryset = LogisticsManagement.objects.all()
    serializer_class = LogisticsManagementSerializer
     
    def get_queryset(self):
        queryset = LogisticsManagement.objects.all()  

        # Optional filters via query parameters
        activity = self.request.query_params.get("activity")   

        if activity:
            queryset = queryset.filter(activity__icontains=activity)           

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = LogisticsManagementSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()   
            return Response(
                {"message": "Logistics management details created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogisticsManagementCountView(generics.GenericAPIView):
    """
    GET /api/expenses/count/        -> total expenses
    GET /api/expenses/count/?expense_type=
    GET /api/expenses/count/?flock=
    GET /api/expenses/count/?payment_method=

    """   
    queryset = LogisticsManagement.objects.all()    

    def get(self, request, *args, **kwargs):   
        queryset = LogisticsManagement.objects.all()     

        activity = request.query_params.get("activity")

        if activity:
            queryset = queryset.filter(activity__icontains=activity)


        return Response({"count": queryset.count()})
       