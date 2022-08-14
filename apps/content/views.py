from django.shortcuts import render
from apps.core.models import Article    

def item_details_view(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, f'public/articles/{article.template_name}', {'article': article})
