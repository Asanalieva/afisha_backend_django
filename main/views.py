from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CinemaSerializer, MovieSerializer, ReviewSerializer, GenreSerializer
from main.models import Cinema, Movie, Review, Genre
from rest_framework import status


@api_view(['GET'])
def print_cinema(request):
    cinema = Cinema.objects.all()
    data = CinemaSerializer(cinema, many=True).data
    return Response(data=data)


@api_view(['GET'])
def print_cinema_id(request, id):
    try:
        cinemas = Cinema.objects.get(id=id)
    except Cinema.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Cinema does not exist!'})
    data = CinemaSerializer(cinemas, many=True).data
    return Response(data=data)


@api_view(['GET'])
def print_movie(request):
    word = request.query_params.get('search', '')
    movies = Movie.objects.filter(cinema__name__contains=word)
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def print_movie_id(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie does not exist!'})
    data = MovieSerializer(movies).data
    return Response(data=data)

@api_view(['GET'])
def print_review(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def print_genres(request):
    genres = Genre.objects.all()
    data = GenreSerializer(genres, many=True).data
    return Response(data=data)

@api_view(['PUT','DELETE'])
def delete_put_movie(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == 'PUT':
        movie.title = request.data.get('title','')
        movie.save()
        return Response(data={'message':'Movie updated'})
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message':'Movie Deleted'})

@api_view(['POST'])
def create_movie(request):
    title = request.data.get('title')
    description = request.data.get('description')
    cinema = request.data.get('cinema')
    genres = request.data.get('genres')
    Movie.objects.create(title=title,description=description,cinema=cinema,genres=genres)
    return Response(data={'message': 'Movie Created!'})
