from rest_framework import serializers

from .models import Category, Forecast, Sale, Store


class CategorySerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Category
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Store
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Sale
        fields = "__all__"


class ForecastSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Forecast
        fields = "__all__"
