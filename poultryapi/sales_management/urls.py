from django.urls import path
from .views import SalesManagementView, SalesManagementCountView

urlpatterns = [
    path('', SalesManagementView.as_view(), name='salesmanagement-list-create'),
    path('count/', SalesManagementCountView.as_view(), name='salesmanagement-count'),
]
                                                         