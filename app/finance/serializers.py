
from rest_framework import serializers
from .models import Currency, Cryptocurrency, Commodity, Stock, Inflation

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class InflationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflation
        fields = ['id', 'rate', 'datetime']
