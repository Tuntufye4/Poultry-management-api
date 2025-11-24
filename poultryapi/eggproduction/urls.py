from django.urls import path
from .views import EggproductionListCreateView, EggproductionCountView

urlpatterns = [
    path('', EggproductionListCreateView.as_view(), name='eggproduction-list-create'),
    path('count/', EggproductionCountView.as_view(), name='eggproduction-count'),
]
                      