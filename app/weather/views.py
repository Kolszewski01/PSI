from rest_framework import viewsets, permissions
from .models import Weather, AirQuality
from .serializers import WeatherSerializer, AirQualitySerializer

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAdminOrReadOnly]



class AirQualityViewSet(viewsets.ModelViewSet):
    queryset = AirQuality.objects.all()
    serializer_class = AirQualitySerializer
    permission_classes = [IsAdminOrReadOnly]
