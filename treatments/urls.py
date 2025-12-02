from django.urls import path
from .views import TreatmentListCreateView, TreatmentCountView
        
urlpatterns = [
    path('', TreatmentListCreateView.as_view(), name='treatments-list-create'),
    path('count/', TreatmentCountView.as_view(), name='treatments-count'),
]
                                  