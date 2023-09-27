from django.contrib import admin

from .models import Category, Forecast, Sale, Store


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административная панель для модели Category."""

    list_display = ("sku", "group", "category", "subcategory", "uom")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Административная панель для модели Store."""

    list_display = [
        "store",
        "city",
        "division",
        "type_format",
        "loc",
        "size",
        "is_active",
    ]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """Административная панель для модели Sale."""

    list_display = [
        "store",
        "sku",
        "date",
        "sales_type",
        "sales_units",
        "sales_units_promo",
        "sales_rub",
        "sales_run_promo",
    ]


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    """Административная панель для модели Forecast."""

    list_display = ["store", "forecast_date", "sku", "sales_units_forecasted"]
