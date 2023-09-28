from rest_framework import serializers

from sale.models import Category, Forecast, Sale, Store


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории товаров"""

    class Meta:
        model = Category
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    """Сериализатор магазина"""

    class Meta:
        model = Store
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    """Сериализатор продаж"""

    class Meta:
        model = Sale
        fields = "__all__"


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза"""

    class Meta:
        model = Forecast
        fields = "__all__"
