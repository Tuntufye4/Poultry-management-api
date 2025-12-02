from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Count

from .models import Flocksetup
from .serializers import FlocksetupSerializer


class FlocksetupListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/flocksetup/      -> list all flocks (with optional filters)
    POST /api/flocksetup/      -> create a new flock
    """
    queryset = Flocksetup.objects.all()   
    serializer_class = FlocksetupSerializer
     
    def get_queryset(self):
        queryset = Flocksetup.objects.all()

        # Optional filters via query parameters   
        breed = self.request.query_params.get("breed")
        poultry_house = self.request.query_params.get("poultry_house")  
        category = self.request.query_params.get("category") 
        source_supplier = self.request.query_params.get("source_supplier") 

        if breed:
            queryset = queryset.filter(breed__icontains=breed)

        if poultry_house:
            queryset = queryset.filter(poultry_house__icontains=poultry_house)   

        if category:
            queryset = queryset.filter(category__icontains=category)

        if source_supplier:   
            queryset = queryset.filter(source_supplier__icontains=source_supplier)

        return queryset

    def post(self, request, *args, **kwargs):
        serializer = FlocksetupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Flock created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlockCountView(generics.GenericAPIView):
    """
    GET /api/flocksetup/count/        
    GET /api/flocksetup/count/?breed=
    GET /api/flocksetup/count/?poultry_house=
    GET /api/flocksetup/count/?category=
    GET /api/flocksetup/count/?source_supplier=
    """   
    queryset = Flocksetup.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Flocksetup.objects.all()

        breed = request.query_params.get("breed")
        poultry_house = request.query_params.get("poultry_house")
        category = request.query_params.get("category")
        source_supplier = request.query_params.get("source_supplier")

        if breed:
            queryset = queryset.filter(breed__icontains=breed)

        if poultry_house:
            queryset = queryset.filter(poultry_house__icontains=poultry_house)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if source_supplier:
            queryset = queryset.filter(source_supplier__icontains=source_supplier)

        return Response({"count": queryset.count()})
   