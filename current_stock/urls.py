from django.urls import path
from .views import CurrentStockListCreateView, CurrentStockCountView

urlpatterns = [
    path('', CurrentStockListCreateView.as_view(), name='currentstock-list-create'),
    path('count/', CurrentStockCountView.as_view(), name='currentstock-count'),
]
                                                             



                                                             