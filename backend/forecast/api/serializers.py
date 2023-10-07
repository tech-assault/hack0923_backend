from rest_framework import serializers
from sale.models import Category, DayForecast, Forecast, Sale, Store


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории товаров."""

    class Meta:
        model = Category
        fields = ("sku", "group", "category", "subcategory", "uom")


class StoreSerializer(serializers.ModelSerializer):
    """Сериализатор магазина."""

    class Meta:
        model = Store
        fields = (
            "store",
            "city",
            "division",
            "type_format",
            "loc",
            "size",
            "is_active",
        )


class SaleRetrieveSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""

    class Meta:
        model = Sale
        exclude = ("id", "store", "sku")


class SaleListSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""

    class Meta:
        model = Sale
        exclude = (
            "id",
            "store",
        )


class DayForecastSerializer(serializers.ModelSerializer):
    """Сериализатор для модели DayForecast."""

    class Meta:
        model = DayForecast
        fields = ("date", "units")


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза."""

    store = serializers.SlugRelatedField(
        slug_field="store", queryset=Store.objects.all()
    )
    sku = serializers.SlugRelatedField(
        slug_field="sku", queryset=Category.objects.all()
    )
    forecast = DayForecastSerializer(many=True)

    class Meta:
        model = Forecast
        fields = ("store", "sku", "forecast_date", "forecast")

    def to_representation(self, instance):
        """
        Преобразует объект прогноза в формат для представления.

        Args:
            instance: Объект прогноза.

        Returns:
            dict: Сериализованный прогноз в нужном формате.
        """
        forecast = super().to_representation(instance)
        forecast["forecast"] = {
            day_forecast["date"]: day_forecast["units"]
            for day_forecast in forecast["forecast"]
        }
        return forecast

    def to_internal_value(self, data):
        """
        Преобразует данные внутреннего представления.

        Args:
            data: Входные данные.

        Returns:
            dict: Преобразованные внутренние данные.
        """
        data["forecast"] = [
            {"date": date, "units": units} for date, units in data["forecast"].items()
        ]
        return data

    @staticmethod
    def set_days_forecast(instance, days_forecast):
        """Создает и связывает прогнозы дней с объектом прогноза продаж."""
        instance.forecast.bulk_create(
            [
                DayForecast(forecast_sku_of_store=instance, **day_forecast)
                for day_forecast in days_forecast
            ]
        )

    def create(self, validated_data):
        """
        Создает новый объект прогноза.

        Args:
            validated_data (dict): Валидированные данные для создания объекта.

        Returns:
            Forecast: Созданный объект прогноза.
        """
        days_forecast = validated_data.pop("forecast")
        forecast = Forecast.objects.create(
            store_id=validated_data["store"],
            sku_id=validated_data["sku"],
            forecast_date=validated_data["forecast_date"],
        )

        self.set_days_forecast(forecast, days_forecast)

        return forecast


class CategoryDeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.

    Используется только для получения данных.
    """

    sku = serializers.CharField(source="pr_sku_id")
    group = serializers.CharField(source="pr_group_id")
    category = serializers.CharField(source="pr_cat_id")
    subcategory = serializers.CharField(source="pr_subcat_id")
    uom = serializers.IntegerField(source="pr_uom_id")

    class Meta:
        model = Category
        fields = ("sku", "group", "category", "subcategory", "uom")


class StoreDeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Store.

    Используется только для получения данных.
    """

    store = serializers.CharField(source="st_id")
    city = serializers.CharField(source="st_city_id")
    division = serializers.CharField(source="st_division_code")
    type_format = serializers.IntegerField(source="st_type_format_id")
    loc = serializers.IntegerField(source="st_type_loc_id")
    size = serializers.IntegerField(source="st_type_size_id")
    is_active = serializers.BooleanField(source="st_is_active")

    class Meta:
        model = Store
        fields = (
            "store",
            "city",
            "division",
            "type_format",
            "loc",
            "size",
            "is_active",
        )


class SaleDeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Sale.

    Используется только для получения данных.
    """

    store = serializers.SlugRelatedField(
        slug_field="store", source="st_id", queryset=Store.objects.all()
    )
    sku = serializers.SlugRelatedField(
        slug_field="sku", source="pr_sku_id", queryset=Category.objects.all()
    )
    date = serializers.DateField()
    sales_type = serializers.IntegerField(source="pr_sales_type_id")
    sales_units = serializers.IntegerField(source="pr_sales_in_units")
    sales_units_promo = serializers.IntegerField(source="pr_promo_sales_in_units")
    sales_rub = serializers.FloatField(source="pr_sales_in_rub")
    sales_run_promo = serializers.FloatField(source="pr_promo_sales_in_rub")

    class Meta:
        model = Sale
        fields = (
            "store",
            "sku",
            "date",
            "sales_type",
            "sales_units",
            "sales_units_promo",
            "sales_rub",
            "sales_run_promo",
        )
