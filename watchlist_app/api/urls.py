from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # Function Based View
    # path('list/', movie_list , name = 'movie_list'),
    # path('<int:pk>', movie_details , name = 'movie_details'),

    # Class Based View (APIVIEW)
    path('list/', MovieListAV.as_view() , name = 'movie_list'),
    path('<int:pk>', MovieDetailAV.as_view() , name = 'movie_details'),

]