from django.urls import path
from .views import HomeView

app_name = 'core'
urlpatterns = [
    path('page/<int:page>/', HomeView.as_view(), name='home'),
]