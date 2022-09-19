from django.contrib import admin
from django.urls import path, include
from watchlist_app.views import movie_details, movie_list

urlpatterns = [
    path('list/', movie_list , name = 'movie_list'),
    path('<int:pk>', movie_details , name = 'movie_details'),
]