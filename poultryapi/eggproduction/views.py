from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Eggproduction
from .serializers import EggproductionSerializer


class EggproductionListCreateView(generics.ListCreateAPIView):
    """    
    GET  /api/eggproduction/      -> list all eggproduction (with optional filters)   
    POST /api/eggproduction/      -> create a new egg production list
    """
    queryset = Eggproduction.objects.all()          
    serializer_class = EggproductionSerializer       
     
    def get_queryset(self):    
        queryset = Eggproduction.objects.all()
   
        # Optional filters via query parameters
        cracked_eggs = self.request.query_params.get("cracked_eggs")
        broken_eggs = self.request.query_params.get("broken_eggs")   
        flock = self.request.query_params.get("flock")  

        if cracked_eggs:
            queryset = queryset.filter(cracked_eggs__icontains=cracked_eggs)

        if broken_eggs:   
            queryset = queryset.filter(broken_eggs__icontains=broken_eggs)  

        if flock:       
            queryset = queryset.filter(flock__icontains=flock)  

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = EggproductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Eggproduction created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,   
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EggproductionCountView(generics.GenericAPIView):
    """
    GET /api/eggproduction/count/        -> total eggproduction
    GET /api/eggproduction/count/?flock=
    GET /api/eggproduction/count/?cracked_eggs=  
    """
    queryset = Eggproduction.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Eggproduction.objects.all()

        cracked_eggs = request.query_params.get("cracked_eggs")
        broken_eggs = request.query_params.get("broken_eggs")
        flock = request.query_params.get("flock")
         
        if cracked_eggs:
            queryset = queryset.filter(cracked_eggs__icontains=cracked_eggs)

        if broken_eggs:    
            queryset = queryset.filter(broken_eggs__icontains=broken_eggs)

        if flock:    
            queryset = queryset.filter(flock__icontains=flock)


        return Response({"count": queryset.count()})
