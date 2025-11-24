from django.urls import path
from .views import NutritionListCreateView, NutritionCountView

urlpatterns = [
    path('', NutritionListCreateView.as_view(), name='nutrition-list-create'),
    path('count/', NutritionCountView.as_view(), name='nutrition-count'),
]
               