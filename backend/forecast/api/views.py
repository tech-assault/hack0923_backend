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
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Category.

    Позволяет просматривать информацию о категориях.
    Поддерживает фильтрацию данных по заданным критериям.
    """

    renderer_classes = (CustomRenderer,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    schema = AutoSchema()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


@extend_schema(tags=["Магазины"])
@extend_schema_view(
    list=extend_schema(
        summary="Список магазинов",
        description="Возвращает список магазинов с возможностью фильтрации и поиска.",
        parameters=[
            OpenApiParameter(
                name="type_format",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Формат магазина для фильтрации.",
            ),
            OpenApiParameter(
                name="loc",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Тип локации магазина для фильтрации и поиска.",
            ),
            OpenApiParameter(
                name="city",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Город магазина для фильтрации и поиска.",
            ),
            OpenApiParameter(
                name="division",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Подразделение магазина для фильтрации и поиска.",
            ),
        ],
        responses={200: StoreSerializer(many=True)},
    ),
)
class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для модели Store.
    
    Позволяет просматривать информацию о магазинах.
    Поддерживает фильтрацию и поиск по формату, локации, городу и подразделению.
    """
    
    renderer_classes = (CustomRenderer,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = StoreFilter
    search_fields = ["type_format", "loc", "city", "division"]


@extend_schema(tags=["Sale"])
@extend_schema_view(
    list=extend_schema(
        summary="Список продаж",
        description="Возвращает список продаж сгруппированных по SKU.",
        parameters=[
            OpenApiParameter(
                name="store",
                type=str,
                location=OpenApiParameter.QUERY,
                description="ID магазина для фильтрации продаж.",
            ),
        ],
        responses={200: SaleListSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Информация о продажах",
        description="Возвращает данные о продажах для заданного SKU и ID магазина.",
        parameters=[
            OpenApiParameter(
                name="store",
                type=str,
                location=OpenApiParameter.QUERY,
                description="ID магазина для фильтрации продаж.",
            ),
            OpenApiParameter(
                name="sku",
                type=str,
                location=OpenApiParameter.QUERY,
                description="SKU товара для фильтрации продаж.",
            ),
        ],
        responses={200: SaleRetrieveSerializer(many=True)},
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
        """
        Возвращает класс сериализатора в зависимости от выполняемого действия.

        Returns:
            type: Класс сериализатора для текущего действия.
        """
        if self.action == 'list':
            return SaleListSerializer
        return SaleRetrieveSerializer

    def list(self, request, *args, **kwargs):
        """
        Возвращает список продаж сгруппированных по SKU.

        Args:
            request (Request): HTTP-запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные ключевые аргументы.

        Returns:
            Response: HTTP-ответ с данными о продажах, сгруппированными по SKU.
        """
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
        """
        Возвращает данные о продажах для заданного SKU и ID магазина.

        Args:
            request (Request): HTTP-запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные ключевые аргументы.

        Returns:
            Response: HTTP-ответ с данными о продажах для заданного SKU и ID магазина.
        """
        queryset = self.get_queryset().filter(
            sku_id=self.request.query_params.get("sku"))
        return Response({'store': self.request.query_params.get('store'),
                         'sku': self.request.query_params.get('sku'),
                         'fact': self.get_serializer(
                             queryset, many=True).data})


@extend_schema(tags=["Прогнозы"])
@extend_schema_view(
    create=extend_schema(
        summary="Создать прогноз",
        description="Создает новый прогноз на основе предоставленных данных.",
        request=ForecastSerializer,
        responses={201: ForecastSerializer(many=True)},
    ),
    list=extend_schema(
        summary="Список прогнозов",
        description="Возвращает список прогнозов с возможностью фильтрации по SKU и ID магазина.",
        parameters=[
            OpenApiParameter(
                name="sku",
                type=str,
                location=OpenApiParameter.QUERY,
                description="SKU товара для фильтрации прогнозов.",
            ),
            OpenApiParameter(
                name="store",
                type=str,
                location=OpenApiParameter.QUERY,
                description="ID магазина для фильтрации прогнозов.",
            ),
        ],
        responses={200: ForecastSerializer(many=True)},
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
        """
        Возвращает набор данных прогнозов для заданных SKU и ID магазина.

        Returns:
            QuerySet: Набор данных прогнозов, соответствующих заданным SKU и ID магазина.
        """
        sku = self.request.query_params.get("sku")
        store = self.request.query_params.get("store")
        return Forecast.objects.filter(sku_id=sku, store_id=store)

    def create(self, request, *args, **kwargs):
        """
        Создает новые прогнозы на основе предоставленных данных.

        Args:
            request (Request): HTTP-запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные ключевые аргументы.

        Returns:
            Response: HTTP-ответ с созданными прогнозами или сообщением об ошибке.
        """
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
