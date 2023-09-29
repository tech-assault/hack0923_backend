from django_filters import rest_framework as filters
from sale.models import Forecast, Store


class ForecastFilter(filters.FilterSet):
    """Фильтр для модели Forecast, позволяющий фильтровать прогнозы по дате."""

    forecast_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Forecast
        fields = ["forecast_date"]


class StoreFilter(filters.FilterSet):
    """Фильтр для модели Store, позволяющий фильтровать магазины по разным полям."""

    class Meta:
        model = Store
        fields = [
            "store",
            "city",
            "division",
            "type_format",
            "loc",
            "size",
            "is_active",
        ]
