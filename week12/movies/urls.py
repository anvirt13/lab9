from django.urls import path
from .views import *

urlpatterns = [
    path('', movies, name="movies"),
    path('movie/<int:pk>', movie, name="movie"),
    path('add', addMovie, name="add"),
    path('update/<int:pk>', updateMovie, name="update"),
    path('delete/<int:pk>', deleteMovie, name="delete"),
    path('review/<int:pk>', reviewMovie, name="review"),
    path('delete_review/<int:pk>', deleteReview, name="delete_review"),
    path('edit_review/<int:pk>', editReview, name="edit_review"),
    path('login', loginPage, name="login"),
    path('logout', logoutUser, name="logout"),
    path('register', registerUser, name="register"),




]