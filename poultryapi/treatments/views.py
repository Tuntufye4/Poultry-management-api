from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count
    
from .models import Treatment
from .serializers import TreatmentSerializer

   
class TreatmentListCreateView(generics.ListCreateAPIView):
    """       
    GET  /api/treatments/      -> list all treatments (with optional filters)   
    POST /api/treatments/      -> create a new treatment
    """    
    queryset = Treatment.objects.all()    
    serializer_class = TreatmentSerializer   
         
    def get_queryset(self):
        queryset = Treatment.objects.all()   

        # Optional filters via query parameters
        flock = self.request.query_params.get("flock")
        trays_sold = self.request.query_params.get("trays_sold") 
        treatment_type = self.request.query_params.get("treatment_type")   
    
        if flock:
            queryset = queryset.filter(flock__icontains=flock)
 
        if trays_sold:
            queryset = queryset.filter(trays_sold__icontains=trays_sold)  

        if treatment_type:
            queryset = queryset.filter(treatment_type__icontains=treatment_type)    

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Treatments created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TreatmentCountView(generics.GenericAPIView):
    """
    GET /api/treatments/count/        -> total treatments  
    GET /api/treatments/count/?treatment_type       
    """   
    queryset = Treatment.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Treatment.objects.all()    

        flock = request.query_params.get("flock")
        treatment_type = request.query_params.get("treatment_type")
        trays_sold = request.query_params.get("trays_sold")
     
        if flock:     
            queryset = queryset.filter(flock__icontains=flock)   

        if trays_sold:
            queryset = queryset.filter(trays_sold__icontains=trays_sold)

        if treatment_type:
            queryset = queryset.filter(treatment_type__icontains=treatment_type)
   
        return Response({"count": queryset.count()})
