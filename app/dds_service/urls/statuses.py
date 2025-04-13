from django.urls import path
from dds_service.views import statuses

urlpatterns = [

    path('', statuses.list, name='statuses_list'),
    path('new/', statuses.create, name='statuses_create'),
    path('edit/<int:pk>/', statuses.edit, name='statuses_edit'),
    path('delete/<int:pk>/', statuses.delete, name='statuses_delete'),
]