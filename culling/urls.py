from django.urls import path
from .views import CullingListCreateView, CullingCountView   

urlpatterns = [
    path('', CullingListCreateView.as_view(), name='culling-list-create'),
    path('count/', CullingCountView.as_view(), name='culling-count'),
]
                  