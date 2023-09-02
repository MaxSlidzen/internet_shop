from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    MessageCreateView, choose_version, IndexView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products', ProductListView.as_view(), name='product_list'),
    path('product_<int:pk>_<str:slug>/view/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product_<int:pk>_<str:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product_<int:pk>_<str:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_<int:pk>_<str:version_id>/choose_version/', choose_version, name='choose_version'),
    path('contacts/', MessageCreateView.as_view(), name='contacts')
]
