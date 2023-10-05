from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, extend_schema, \
    extend_schema_view, inline_serializer, OpenApiResponse
from drf_standardized_errors.openapi import AutoSchema
from rest_framework import filters, mixins, viewsets, status
from rest_framework.response import Response

from sale.models import Category, Forecast, Sale, Store

from .filters import CategoryFilter, ForecastFilter, StoreFilter
from .serializers import (
    CategorySerializer,
    ForecastDeSerializer,
    ForecastSerializer,
    SaleSerializer,
    StoreSerializer,
)
from .utils import CustomRenderer


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
    renderer_class = CustomRenderer

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    schema = AutoSchema()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


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
    renderer_class = CustomRenderer

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = StoreFilter
    search_fields = ["type_format", "loc", "city", "division"]


@extend_schema(tags=["Sale"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список продаж",
        description="Возвращает список продаж для заданного SKU и ID магазина.",
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара",
                             required=True),
            OpenApiParameter(name="store", description="ID магазина",
                             required=True),
        ],
    ),
    retrieve=extend_schema(
        summary="Получить детали продажи",
        description="Возвращает детали продажи для заданного ID.",
    ),
)
class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Sale."""
    renderer_class = CustomRenderer

    serializer_class = SaleSerializer
    schema = AutoSchema()

    def get_queryset(self):
        """Возвращает набор данных продаж для заданного SKU и ID магазина."""
        return Sale.objects.filter(
            sku=self.request.query_params.get("sku"),
            store_id=self.request.query_params.get("store"))

    def list(self, request, *args, **kwargs):
        return Response({'store': self.request.query_params.get('store'),
                         'sku': self.request.query_params.get('sku'),
                         'fact': self.get_serializer(
                             self.get_queryset(), many=True).data})


@extend_schema(tags=["Прогнозы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список прогнозов",
        description=(
                "Возвращает список прогнозов для заданных SKU и ID магазина."),
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара",
                             required=True),
            OpenApiParameter(name="store_id", description="ID магазина",
                             required=True),
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
    """
    Вьюсет для модели Forecast.

    Позволяет создавать и просматривать прогнозы.
    Поддерживает фильтрацию прогнозов по SKU, ID магазина и дате.
    """

    schema = AutoSchema()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ForecastFilter

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
