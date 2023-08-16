from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # path('contacts/', MessageCreateView.as_view(), name='contacts'),
]
