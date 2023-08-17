from django.shortcuts import render
from blog.models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from pytils.translit import slugify


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title': 'Статья',
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview']

    success_url = reverse_lazy('blog:article_list')
    extra_context = {
        'title': 'Создание',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview']

    extra_context = {
        'title': 'Изменение',
    }

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
    extra_context = {
        'title': 'Удаление',
    }
