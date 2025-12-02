from django.urls import path
from .views import MeatsalesListCreateView, MeatsalesCountView

urlpatterns = [
    path('', MeatsalesListCreateView.as_view(), name='meatsales-list-create'),
    path('count/', MeatsalesCountView.as_view(), name='meatsales-count'),
]
                                          