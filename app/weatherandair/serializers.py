from rest_framework import serializers
from .models import Weather, AirQuality

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city', 'temperature', 'humidity', 'precipitation', 'date']
        read_only_fields = ['id', 'date']

class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQuality
        fields = ['id', 'weather', 'quality', 'date']
        read_only_fields = ['id', 'date']
