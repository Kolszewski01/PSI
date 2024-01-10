from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Currency, Cryptocurrency, Commodity, Stock, Inflation
from .serializers import CurrencySerializer, CryptocurrencySerializer, CommoditySerializer, StockSerializer, InflationSerializer


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminOrReadOnly]
class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [IsAdminOrReadOnly]
class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = [IsAdminOrReadOnly]
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrReadOnly]


class InflationViewSet(viewsets.ModelViewSet):
    queryset = Inflation.objects.all()
    serializer_class = InflationSerializer
    permission_classes = [IsAdminOrReadOnly]
