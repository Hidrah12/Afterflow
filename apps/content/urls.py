from django.urls import path
from .views import item_details_view

app_name = 'content'
urlpatterns = [
    path('<slug:slug>/', item_details_view, name='item-details'),
]