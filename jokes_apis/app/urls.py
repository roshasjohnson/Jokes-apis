from django.urls import path
from .views import fetch_jokes, JokeListView

urlpatterns = [
    path('fetch-jokes/', fetch_jokes, name='fetch_jokes'),
    path('jokes/', JokeListView.as_view(), name='joke_list'),
]
