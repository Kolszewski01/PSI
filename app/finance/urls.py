from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, CryptocurrencyViewSet, CommodityViewSet, StockViewSet, InflationViewSet

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'cryptocurrencies', CryptocurrencyViewSet)
router.register(r'commodities', CommodityViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'inflation', InflationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
