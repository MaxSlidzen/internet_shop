from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    MessageCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product_<int:pk>_<str:slug>/view/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product_<int:pk>_<str:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product_<int:pk>_<str:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', MessageCreateView.as_view(), name='contacts')
]
