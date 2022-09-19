from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.



# Function Basec View
def movie_list(request):
  '''Convert : Complex Data Type --> Python Dic --> Python Json'''
  
  movies =Movie.objects.all()
  data = {
    'movies' : list(movies.values())
  }
  print(data)
  return JsonResponse(data)


def movie_details(request, pk):
  print(pk)
  movie =Movie.objects.get(pk= pk)
  
  data = {
    'name' : movie.name,
    'description' : movie.description,
    'active' : movie.active,
  }
  
  return JsonResponse(data)