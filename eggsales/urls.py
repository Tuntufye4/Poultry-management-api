from django.urls import path
from .views import EggsalesListCreateView, EggsalesCountView

urlpatterns = [
    path('', EggsalesListCreateView.as_view(), name='eggsales-list-create'),
    path('count/', EggsalesCountView.as_view(), name='eggsales-count'),
]
                            