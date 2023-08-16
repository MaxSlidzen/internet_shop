from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    # path('contacts/', MessageCreateView.as_view(), name='contacts'),
    # path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
