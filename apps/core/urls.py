from django.urls import path
from .views import articles_from_a_category_view, HomeView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articulos/<str:category_name>/', articles_from_a_category_view, name='articles-from-category'),
]