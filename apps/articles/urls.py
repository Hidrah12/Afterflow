from django.urls import path
from .views import detail_article

app_name = 'articles'
urlpatterns = [
    path('<slug:slug>/', detail_article, name='detail-article'),
]