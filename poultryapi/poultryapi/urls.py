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
    path('api/inventory_movement/', include('inventory_movement.urls')),
    path('api/farm_management/', include('farm_management.urls')),
    path('api/logistics_management/', include('logistics_management.urls')),
    path('api/sales_management/', include('sales_management.urls')),
    path('api/meatsales/', include('meatsales.urls')),   
    path('api/auth/', include('users.urls')),
]
                                                       