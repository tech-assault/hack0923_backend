from rest_framework import serializers

from sale.models import Category, Forecast, Sale, Store


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


class SaleSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""

    store = serializers.SlugRelatedField(
        slug_field="store", queryset=Store.objects.all()
    )
    sku = serializers.SlugRelatedField(
        slug_field="sku", queryset=Category.objects.all()
    )

    class Meta:
        model = Sale
        fields = "__all__"


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза."""

    store = serializers.SlugRelatedField(
        slug_field="store", queryset=Store.objects.all()
    )
    sku = serializers.SlugRelatedField(
        slug_field="sku", queryset=Category.objects.all()
    )

    class Meta:
        model = Forecast
        fields = ("store", "forecast_date", "sku", "sales_units_forecasted")


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


class ForecastDeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Forecast.

    Используется только для получения данных.
    """

    store = serializers.SlugRelatedField(
        slug_field="store", source="st_id", queryset=Store.objects.all()
    )
    forecast_date = serializers.DateField()
    sku = serializers.SlugRelatedField(
        slug_field="sku", source="pr_sku_id", queryset=Category.objects.all()
    )
    sales_units_forecasted = serializers.IntegerField(source="target")

    class Meta:
        model = Forecast
        fields = ("store", "forecast_date", "sku", "sales_units_forecasted")
