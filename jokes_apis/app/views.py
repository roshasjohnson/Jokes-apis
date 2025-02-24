import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Joke
import json

from rest_framework.generics import ListAPIView
from .models import Joke
from .serializers import JokeSerializer

JOKES_API = 'https://v2.jokeapi.dev/joke/Any?amount=100'


@api_view(['GET'])
def fetch_jokes (request):
    response = requests.get(JOKES_API)
    jokes = response.json()
   
    if "jokes" in jokes:
        for joke in jokes["jokes"]:
            Joke.objects.create(
                category=joke['category'],
                type=joke['type'],
                joke=joke.get('joke', ''),  
                setup=joke.get('setup', ''),  
                lang=joke['lang'],
                safe=joke['safe'],
                nsfw=joke['flags']['nsfw'],
                political=joke['flags']['political'],
                sexist=joke['flags']['sexist']
            )
    
    return Response({"message": "Jokes fetched and stored successfully!"}, status=status.HTTP_201_CREATED)



class JokeListView(ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer