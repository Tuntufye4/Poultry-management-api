from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Flock setup API routes
    path('api/flocksetup/', include('flocksetup.urls')),  
    path('api/nutritionworkflow/', include('nutritionworkflow.urls')), 
    path('api/inventory/', include('inventory.urls')),    
    path('api/culling/', include('culling.urls')), 
    path('api/expenses/', include('expenses.urls')),          
    path('api/eggsales/', include('eggsales.urls')), 
    path('api/manuresales/', include('manuresales.urls')), 
    path('api/treatments/', include('treatments.urls')), 
    path('api/meatproduction/', include('meatproduction.urls')), 
    path('api/eggproduction/', include('eggproduction.urls')),     
]
                 