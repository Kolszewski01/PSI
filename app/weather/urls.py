from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet, AirQualityViewSet

router = DefaultRouter()
router.register(r'Weather', WeatherViewSet)
router.register(r'Air_Quality', AirQualityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
