from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CinemaSerializer
from main.models import Cinema
from rest_framework import status
@api_view(['GET'])
def print_movie(request):
    cinema = Cinema.objects.all()
    data = CinemaSerializer(cinema, many=True).data
    return Response(data=data)

@api_view(['GET'])
def print_movie_id(request,id):
    try:
        cinemas = Cinema.objects.get(id=id)
    except Cinema.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Cinema does not exists'})
    data = CinemaSerializer(cinemas).data
    return Response(data=data)
