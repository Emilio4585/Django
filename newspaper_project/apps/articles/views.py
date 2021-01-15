from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title','body',)
    template_name = 'articles/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body', 'author')
#http://127.0.0.1:8000/articles