from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from drf_standardized_errors.openapi import AutoSchema
from rest_framework import filters, mixins, viewsets, status
from rest_framework.response import Response

from sale.models import Category, Forecast, Sale, Store

from .filters import CategoryFilter, ForecastFilter, StoreFilter
from .serializers import (CategorySerializer, ForecastSerializer,
                          StoreSerializer, SaleListSerializer,
                          SaleRetrieveSerializer)
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
    renderer_classes = (CustomRenderer,)

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
    renderer_classes = (CustomRenderer,)

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
            OpenApiParameter(name="store", description="ID магазина",
                             required=True),
        ],
    ),
    retrieve=extend_schema(
        summary="Получить детали продажи",
        description="Возвращает детали продажи для заданного ID.",
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара",
                             required=True),
            OpenApiParameter(name="store", description="ID магазина",
                             required=True),
        ],
    ),
)
class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Sale."""
    renderer_classes = (CustomRenderer,)

    schema = AutoSchema()

    def get_queryset(self):
        """Возвращает набор данных продаж для заданного SKU и ID магазина."""
        return Sale.objects.filter(
            store_id=self.request.query_params.get("store"))

    def get_serializer_class(self):
        if self.action == 'list':
            return SaleListSerializer
        return SaleRetrieveSerializer

    def list(self, request, *args, **kwargs):
        result = []
        sku_indexs = {}
        store = self.request.query_params.get('store')
        for purchase in self.get_serializer(
                self.get_queryset(), many=True).data:
            sku = purchase.pop('sku')
            if sku not in sku_indexs:
                sku_indexs[sku] = len(result)
                result.append({'store': store, 'sku': sku, 'fact': [purchase]})
            else:
                result[sku_indexs[sku]]['fact'].append(purchase)

        return Response(result)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            sku_id=self.request.query_params.get("sku"))
        return Response({'store': self.request.query_params.get('store'),
                         'sku': self.request.query_params.get('sku'),
                         'fact': self.get_serializer(
                             queryset, many=True).data})


@extend_schema(tags=["Прогнозы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список прогнозов",
        description=(
                "Возвращает список прогнозов для заданных SKU и ID магазина."),
        parameters=[
            OpenApiParameter(name="sku", description="SKU товара",
                             required=True),
            OpenApiParameter(name="store", description="ID магазина",
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
    renderer_classes = (CustomRenderer,)
    serializer_class = ForecastSerializer
    schema = AutoSchema()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ForecastFilter

    def get_queryset(self):
        """Возвращает набор данных прогнозов для заданных SKU и ID магазина."""
        sku = self.request.query_params.get("sku")
        store = self.request.query_params.get("store")
        return Forecast.objects.filter(sku_id=sku, store_id=store)

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        result = []
        try:
            for forecast in data:
                serializer = self.get_serializer(data=forecast)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                result.append(serializer.data)
        except IntegrityError as error_message:
            return Response({'error': str(error_message)},
                            status=status.HTTP_409_CONFLICT)

        headers = self.get_success_headers(result)
        return Response(result, status=status.HTTP_201_CREATED,
                        headers=headers)
