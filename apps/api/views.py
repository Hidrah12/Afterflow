from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from apps.core.models import Article
from rest_framework.response import Response

COUNT_ARTICLES = 8

@api_view(['GET'])
def set_count(request):
    global COUNT_ARTICLES
    COUNT_ARTICLES = 8
    return Response({"Message": "Exitoso"})

@api_view(["GET"])
def get_more_articles(request):
    global COUNT_ARTICLES
    articles = Article.objects.all().order_by('-id')

    if COUNT_ARTICLES + 8 < articles.count():
        articles = articles[COUNT_ARTICLES:COUNT_ARTICLES + 8]
        COUNT_ARTICLES += 8
        articles_json = ArticleSerializer(articles, many=True)
        return Response(articles_json.data)
    
    elif COUNT_ARTICLES + 8 >= articles.count():
        articles = articles[COUNT_ARTICLES:]
        COUNT_ARTICLES = 8
        articles_json = ArticleSerializer(articles, many=True)
        return Response(articles_json.data + [{"Message": "No more articles"}])
