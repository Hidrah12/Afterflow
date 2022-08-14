from .models import Article
from django.shortcuts import render
from django.views.generic import ListView

class HomeView(ListView):
    context_object_name = 'articles'
    template_name = 'public/index.html'

    def get_queryset(self):
        self.articles = Article.objects.all().order_by('-id')[:8]
        return self.articles
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.articles.count()
        return context

def articles_from_a_category_view(request, category_name):
    articles = Article.objects.filter(category_for_development = category_name)

    context_data = {
        'articles': articles,
        'total_items': articles.count(),
        'category_name': category_name
    }
    
    return render(request, 'public/articles/articles-from-category.html', context_data)
