from django.urls import path
from .views import ExpensesView, ExpensesCountView

urlpatterns = [
    path('', ExpensesView.as_view(), name='expenses-list-create'),
    path('count/', ExpensesCountView.as_view(), name='expenses-count'),
]
                                                  