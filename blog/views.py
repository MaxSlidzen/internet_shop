from django.shortcuts import render
from blog.models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Блог'
    }


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title': 'Статья',
    }


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview']

    success_url = reverse_lazy('blog:article_list')
    extra_context = {
        'title': 'Создание',
    }


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview']

    extra_context = {
        'title': 'Изменение',
    }

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
    extra_context = {
        'title': 'Удаление',
    }
