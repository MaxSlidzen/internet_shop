from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, MessageCreateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', MessageCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
