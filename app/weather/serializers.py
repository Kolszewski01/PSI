from rest_framework import serializers
from .models import Weather, AirQuality

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'humidity', 'precipitation']



class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQuality
        fields = '__all__'
