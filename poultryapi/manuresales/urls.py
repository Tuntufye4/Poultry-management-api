from django.urls import path
from .views import ManuresalesListCreateView, ManuresalesCountView

urlpatterns = [
    path('', ManuresalesListCreateView.as_view(), name='manuresales-list-create'),
    path('count/', ManuresalesCountView.as_view(), name='manuresales-count'),
]
                                   