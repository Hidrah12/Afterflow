from django.urls import path
from .views import item_details

app_name = 'content'
urlpatterns = [
    path('<slug:slug>/', item_details, name='item-details'),
]