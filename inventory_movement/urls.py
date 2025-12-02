from django.urls import path
from .views import InventorymovementListCreateView, InventorymovementCountView

urlpatterns = [
    path('', InventorymovementListCreateView.as_view(), name='inventorymove-list-create'),
    path('count/', InventorymovementCountView.as_view(), name='inventorymove-count'),
]
                  