from django.urls import path
from .views import SalesListCreateView, SalesCountView

urlpatterns = [
    path('', SalesListCreateView.as_view(), name='sales-list-create'),
    path('count/', SalesCountView.as_view(), name='sales-count'),
]
                          