from django.urls import path
from .views import FarmManagementView, FarmManagementCountView

urlpatterns = [
    path('', FarmManagementView.as_view(), name='farmmanagement-list-create'),
    path('count/', FarmManagementCountView.as_view(), name='farmmanagement-count'),
]
                                                     