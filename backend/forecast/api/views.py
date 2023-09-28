from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from drf_standardized_errors.openapi import AutoSchema
from rest_framework import filters, mixins, viewsets
from sale.models import Category, Forecast, Sale, Store

from .serializers import (
    CategorySerializer,
    ForecastDeSerializer,
    ForecastSerializer,
    SaleSerializer,
    StoreSerializer,
)


@extend_schema(tags=["Категории"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список категорий",
        description="Возвращает список всех категорий товаров.",
    ),
    retrieve=extend_schema(
        summary="Получить детали категории",
        description="Возвращает детали конкретной категории товаров.",
    ),
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    schema = AutoSchema()


@extend_schema(tags=["Магазины"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список магазинов",
        description=(
            "Возвращает список всех магазинов. " "Можно добавить фильтры по полям."
        ),
    ),
    retrieve=extend_schema(
        summary="Получить детали магазина",
        description="Возвращает детали конкретного магазина.",
    ),
)
class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Store."""

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["type_format", "loc", "city", "division"]


@extend_schema(tags=["Sale"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список продаж",
        description="Возвращает список продаж для заданного SKU и ID магазина.",
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара", required=True),
            OpenApiParameter(name="store_id", description="ID магазина", required=True),
        ],
    ),
    retrieve=extend_schema(
        summary="Получить детали продажи",
        description="Возвращает детали продажи для заданного ID.",
    ),
)
class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Sale."""

    serializer_class = SaleSerializer
    schema = AutoSchema()

    def get_queryset(self):
        """Возвращает набор данных продаж для заданного SKU и ID магазина."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Sale.objects.filter(sku=sku, store_id=store_id)


@extend_schema(tags=["Прогнозы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список прогнозов",
        description=("Возвращает список прогнозов для заданных SKU и ID магазина."),
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара", required=True),
            OpenApiParameter(name="store_id", description="ID магазина", required=True),
        ],
    ),
    create=extend_schema(
        summary="Создать новый прогноз",
        description=(
            "Принимает спрогнозированные значения для товара и ТЦ," " сохраняет в БД"
        ),
        request=ForecastSerializer,
        responses={201: ForecastSerializer},
    ),
)
class ForecastViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Вьюсет для модели Forecast."""

    schema = AutoSchema()

    def get_queryset(self):
        """Возвращает набор данных прогнозов для заданных SKU и ID магазина."""
        sku = self.request.query_params.get("sku")
        store_id = self.request.query_params.get("store_id")
        return Forecast.objects.filter(pr_sku_id=sku, st_id=store_id)

    def get_serializer_class(self):
        """Функция определяющая сериализатор в зависимости от метода."""
        if self.action == "list":
            return ForecastSerializer
        return ForecastDeSerializer
