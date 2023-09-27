from rest_framework import viewsets

from .models import Category, Forecast, Sale, Store
from .serializers import (
    CategorySerializer,
    ForecastSerializer,
    SaleSerializer,
    StoreSerializer,
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Store."""

    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Sale."""

    def get_queryset(self):
        """."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Sale.objects.filter(sku=sku, store_id=store_id)

    serializer_class = SaleSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Forecast."""

    def get_queryset(self):
        """."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Forecast.objects.filter(sku=sku, store_id=store_id)

    serializer_class = ForecastSerializer
