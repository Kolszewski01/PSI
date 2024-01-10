from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet, AirQualityViewSet

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)
router.register(r'airquality', AirQualityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
