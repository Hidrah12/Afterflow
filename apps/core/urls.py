from django.urls import path
from .views import home_view, articles_from_categorys

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('post/category/<str:category>/', articles_from_categorys, name='articles-from-category'),
]