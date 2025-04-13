from django.urls import path
from dds_service.views import types

urlpatterns = [

    path('', types.list, name='types_list'),
    path('new/', types.create, name='types_create'),
    path('edit/<int:pk>/', types.edit, name='types_edit'),
    path('delete/<int:pk>/', types.delete, name='types_delete'),
]