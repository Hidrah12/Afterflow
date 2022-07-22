from django.shortcuts import render
from apps.core.models import Article    

def detail_article(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, f'articles/{article.template_name}', {'article': article})