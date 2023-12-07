from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes),
    path('movies', getMovies),
    path('movies/<int:pk>', getMovie),




]