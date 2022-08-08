from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, SearchArticleSerializer
from rest_framework.response import Response
from apps.core.models import Article
from rest_framework import status

total_items = 8

@api_view(['GET'])
def set_count(request):
    global total_items

    if request.method == 'GET':
        total_items = 8
        return Response({"Message": "Exitoso"}, status = status.HTTP_200_OK)

    else:
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET"])
def get_more_articles(request):
    global total_items

    if request.method == 'GET':
        articles = Article.objects.all().order_by('-id')

        if total_items + 8 < articles.count():
            articles = articles[total_items:total_items + 8]
            total_items += 8
            articles_json = ArticleSerializer(articles, many=True)
            return Response(articles_json.data, status = status.HTTP_200_OK)
        
        elif total_items + 8 >= articles.count():
            articles = articles[total_items:]
            total_items = 8
            articles_json = ArticleSerializer(articles, many=True)
            return Response(articles_json.data + [{"Message": "No more articles"}], status = status.HTTP_200_OK)

    else:

        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def search_article(request, value):
    if request.method == 'GET':
        articles = Article.objects.filter(title__icontains = value)
        if articles:
            articles_serializer = SearchArticleSerializer(articles, many = True)
            return Response(articles_serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'message': 'No hay coincidencias'}, status = status.HTTP_204_NO_CONTENT)
    else:
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)
