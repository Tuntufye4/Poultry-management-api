from django.urls import path
from .views import InventoryListCreateView, InventoryCountView

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('count/', InventoryCountView.as_view(), name='inventory-count'),
]
                  