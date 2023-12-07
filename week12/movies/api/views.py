from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        'GET /api',
        'GET /api/movies',
        'GET /api/movies/:id',
    ]

    return Response(routes)

@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    seralizer = MovieSerializer(movies, many=True)

    return Response(seralizer.data)

@api_view(['GET'])
def getMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    seralizer = MovieSerializer(movie)

    return Response(seralizer.data)




