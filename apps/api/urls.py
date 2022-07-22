from django.urls import path
from .views import get_more_articles, set_count

app_name = 'api'
urlpatterns = [
    path('', get_more_articles, name='get-more-articles'),
    path('set/', set_count, name='set-count'),
]