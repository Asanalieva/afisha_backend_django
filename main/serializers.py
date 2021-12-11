from rest_framework import serializers
from main.models import Cinema, Movie, Genre, Review


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    #movies = serializers.SerializerMethodField()
    cinema = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True) IN DICT FORMAT
    reviews = serializers.SerializerMethodField()  # WITHOUT DICT FORMAT
    reviews_list = serializers.SerializerMethodField()  # WITHOUT DICT FORMAT

    class Meta:
        model = Movie
        fields = 'id title description cinema genres reviews reviews_list'.split()

    def get_cinema(self, movies):
        return movies.cinema

    def get_genres(self, movies):
        l = []
        for i in movies.genres.all():
            l.append(i.name)
        return l
    # def get_movies(self, movies):
    #     return 0
    def get_reviews(self, movies):
        l = [i.text for i in movies.reviews.all()]
        return l

    def get_reviews_list(self, movies):
        reviews = movies.reviews.exclude(text__contains='covid')  # exclude
        return ReviewSerializer(reviews, many=True).data


class Movie_valid_serializator(serializers.Serializer):
    title = serializers.CharField(min_length=3,max_length=20)
    description = serializers.CharField(min_length=3,max_length=100)
    genres = serializers.ListField(child=serializers.IntegerField())
