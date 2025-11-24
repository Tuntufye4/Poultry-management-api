from django.urls import path
from .views import FlocksetupListCreateView, FlockCountView

urlpatterns = [
    path('', FlocksetupListCreateView.as_view(), name='flocksetup-list-create'),
    path('count/', FlockCountView.as_view(), name='flocksetup-count'),
]
           