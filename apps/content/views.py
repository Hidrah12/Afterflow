from django.shortcuts import render
from apps.core.models import Article

def item_details_view(request, slug):
    article = Article.objects.get(slug = slug)
    recommend = Article.objects.filter(category = article.category)
    return render(request, f'public/articles/{article.template_name}', {'article': article,'recommend': recommend})