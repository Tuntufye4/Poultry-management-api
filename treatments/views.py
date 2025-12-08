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
        treatment_type = self.request.query_params.get("treatment_type")   
        drug_name = self.request.query_params.get("drug_name")
        drug_type = self.request.query_params.get("drug_type")
        administered_by = self.request.query_params.get("administered_by")
    
        if flock:
            queryset = queryset.filter(flock__icontains=flock)
    
        if treatment_type:
            queryset = queryset.filter(treatment_type__icontains=treatment_type)    

        if drug_name:
            queryset = queryset.filter(drug_name__icontains=drug_name)

        if drug_type:
            queryset = queryset.filter(drug_type__icontains=drug_type)

        if administered_by:
            queryset = queryset.filter(administered_by__icontains=administered_by)

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
    GET /api/treatments/count/?flock
    GET /api/treatments/count/?drug_name    
    GET /api/treatments/count/?drug_type    
    GET /api/treatments/count/?administered_by              
    """   
    queryset = Treatment.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Treatment.objects.all()    

        flock = request.query_params.get("flock")
        treatment_type = request.query_params.get("treatment_type")
        drug_name = request.query_params.get("drug_name")
        drug_type = request.query_params.get("drug_type")
        administered_by = request.query_params.get("administered_by")
          
     
        if flock:     
            queryset = queryset.filter(flock__icontains=flock)   

        if treatment_type:
            queryset = queryset.filter(treatment_type__icontains=treatment_type)

        if drug_name:
            queryset = queryset.filter(drug_name__icontains=drug_name)       

        if drug_type:
            queryset = queryset.filter(drug_type__icontains=drug_type)

        if administered_by:
            queryset = queryset.filter(administered_by__icontains=administered_by)
   
        return Response({"count": queryset.count()})
           