from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import CinemaSerializer, MovieSerializer, ReviewSerializer, GenreSerializer, Movie_valid_serializator
from main.models import Cinema, Movie, Review, Genre
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def print_cinema(request):
    cinema = Cinema.objects.all()
    data = CinemaSerializer(cinema, many=True).data
    return Response(data=data)


#

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
    movies = Movie.objects.filter(cinema__movie__title__contains=word)
    context = MovieSerializer(movies, many=True).data
    return Response(data=context)


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


@api_view(['PUT', 'DELETE'])
def delete_put_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        genres = request.data.get('genres')
        serializer = Movie_valid_serializator(data=request.data)
        if serializer.is_valid():
            movie = Movie.objects.create(title=title, description=description)
            return Response(data={'massage': 'Movie changed',
                                  'data': MovieSerializer(movie).data})

        movie = Movie.objects.create(title=title)
        movie.genres.set(genres)
        movie.save()

    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie Deleted'})


@api_view(['POST', 'GET'])
def create_view_movie(request):
    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        genres = request.data.get('genres')
        serializer = Movie_valid_serializator(data=request.data)
        if serializer.is_valid():
            movie = Movie.objects.create(title=title, description=description)
            return Response(data={'massage': 'Movie created',
                                  'data': MovieSerializer(movie).data})


        movie = Movie.objects.create(title=title)
        movie.genres.set(genres)
        movie.save()
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = GenreSerializer(genres, many=True).data
        return Response(data=data)



@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username,password=password)
    if user :
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
            return Response(data={'token':token.key})
    else:
         return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def registration(request):
    username = request.data['username']
    password = request.data['password']
    User.objects.create_user(username=username,
                             password=password)
    return Response(data={'message':'User Created'})

