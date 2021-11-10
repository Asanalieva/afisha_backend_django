from rest_framework import serializers
from main.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = 'id name'.split()
