from django.urls import path
from .views import get_more_articles, set_count, search_article

app_name = 'api'
urlpatterns = [
    path('', get_more_articles, name='get-more-articles'),
    path('set/', set_count, name='set-count'),
    path('search/<str:value>/', search_article, name='search-article'),
]