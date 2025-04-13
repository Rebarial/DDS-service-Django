from django.urls import path
from dds_service.views import subcategories

urlpatterns = [

    path('', subcategories.list, name='subcategories_list'),
    path('new/', subcategories.create, name='subcategories_create'),
    path('edit/<int:pk>/', subcategories.edit, name='subcategories_edit'),
    path('delete/<int:pk>/', subcategories.delete, name='subcategories_delete'),
]