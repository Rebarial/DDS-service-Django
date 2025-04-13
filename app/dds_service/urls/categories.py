from django.urls import path
from dds_service.views import categories

urlpatterns = [

    path('', categories.list, name='categories_list'),
    path('new/', categories.create, name='categories_create'),
    path('edit/<int:pk>/', categories.edit, name='categories_edit'),
    path('delete/<int:pk>/', categories.delete, name='categories_delete'),
]