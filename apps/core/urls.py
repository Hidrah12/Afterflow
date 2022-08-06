from django.urls import path
from .views import articles_from_a_category, HomeView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filter/post/<str:category_name>/', articles_from_a_category, name='articles-from-category'),
]