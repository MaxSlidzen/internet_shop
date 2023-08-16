from django.shortcuts import render
from blog.models import Article
from django.views.generic import ListView


class ArticleListView(ListView):
    model = Article
    extra_context = {
            'title': 'Блог',
            'button': 'Перейти к статье'
        }