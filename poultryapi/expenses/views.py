from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Expenses    
from .serializers import ExpensesSerializer          

    
class ExpensesView(generics.ListCreateAPIView):   
    """      
    GET  /api/expense/      -> list all flocks (with optional filters)      
    POST /api/expense/      -> create a new flock
    """
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
     
    def get_queryset(self):
        queryset = Expenses.objects.all()

        # Optional filters via query parameters
        expense_type = self.request.query_params.get("expense_type")   
        flock = self.request.query_params.get("flock")  
        payment_method = self.request.query_params.get("payment_method")  

        if expense_type:
            queryset = queryset.filter(expense_type__icontains=expense_type)
    
        if flock:
            queryset = queryset.filter(flock__icontains=flock)   

        if payment_method:
            queryset = queryset.filter(payment_method__icontains=payment_method)   
        

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(
                {"message": "Expense created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


