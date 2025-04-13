from django.urls import path
from dds_service.views import transactions

urlpatterns = [

    path('', transactions.list, name='transactions_list'),
    path('new/', transactions.create, name='transactions_create'),
    path('edit/<int:pk>/', transactions.edit, name='transactions_edit'),
    path('delete/<int:pk>/', transactions.delete, name='transactions_delete'),
]