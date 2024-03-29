from django.urls import path
from .views import get_more_articles_api_view, set_count_api_view, search_article_api_view, articles_api_view

app_name = 'api'
urlpatterns = [
    path('', get_more_articles_api_view, name='get-more-articles'),
    path('articles/', articles_api_view, name='articles'),
    path('set/', set_count_api_view, name='set-count'),
    path('buscar/<str:value>/', search_article_api_view, name='search-article'),
]