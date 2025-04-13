from django.contrib import admin
from django.urls import path, include
from dds_service.views import transactions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', transactions.list, name='transactions_list'),

    path('transactions/', include('dds_service.urls.transactions')),

    path('statuses/', include('dds_service.urls.statuses')),

    path('types/', include('dds_service.urls.types')),

    path('categories/', include('dds_service.urls.categories')),

    path('subcategories/', include('dds_service.urls.subcategories')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)