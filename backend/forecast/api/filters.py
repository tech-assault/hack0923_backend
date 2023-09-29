from django_filters import rest_framework as filters
from sale.models import Forecast


class ForecastFilter(filters.FilterSet):
    """Фильтр для модели Forecast, позволяющий фильтровать прогнозы по дате."""

    forecast_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Forecast
        fields = ["forecast_date"]
