from rest_framework import filters, mixins, viewsets

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
    filter_backends = [filters.SearchFilter]
    search_fields = ["type_format", "loc", "city", "division"]


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Sale."""

    serializer_class = SaleSerializer

    def get_queryset(self):
        """Возвращает набор данных продаж для заданного SKU и ID магазина."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Sale.objects.filter(sku=sku, store_id=store_id)


class ForecastViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Вьюсет для модели Forecast."""

    serializer_class = ForecastSerializer

    def get_queryset(self):
        """Возвращает набор данных прогнозов для заданных SKU и ID магазина."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Forecast.objects.filter(sku=sku, store_id=store_id)
