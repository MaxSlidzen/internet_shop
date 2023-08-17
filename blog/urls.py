from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article_<int:pk>_<str:slug>/view/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('article_<int:pk>_<str:slug>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article_<int:pk>_<str:slug>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
