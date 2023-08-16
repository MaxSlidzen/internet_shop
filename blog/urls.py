from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    # path('', ProductListView.as_view(), name='product_list'),
    # path('contacts/', MessageCreateView.as_view(), name='contacts'),
    # path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
