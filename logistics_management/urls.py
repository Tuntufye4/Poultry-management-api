from django.urls import path
from .views import LogisticsManagementView, LogisticsManagementCountView

urlpatterns = [
    path('', LogisticsManagementView.as_view(), name='logisticsmanagement-list-create'),
    path('count/', LogisticsManagementCountView.as_view(), name='logisticsmanagement-count'),
]
                                                        