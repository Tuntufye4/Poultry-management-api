from django.urls import path
from .views import MeatproductionListCreateView, MeatproductionCountView

urlpatterns = [
    path('', MeatproductionListCreateView.as_view(), name='meatproduction-list-create'),
    path('count/', MeatproductionCountView.as_view(), name='meatproduction-count'),
]
                          