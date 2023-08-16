from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product', product, name='product'),
]
