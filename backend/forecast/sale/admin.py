from django.contrib import admin
from django.forms import forms

from import_export.admin import ImportExportModelAdmin

from .models import Category, Forecast, Sale, Store
from .resources import CategoryResource, StoreResource, SaleResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    """Административная панель для модели Category."""
    resource_class = CategoryResource

    list_display = ("sku", "group", "category", "subcategory", "uom")


@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    """Административная панель для модели Store."""
    resource_class = StoreResource

    list_display = ("store", "city", "division", "type_format", "loc", "size",
                    "is_active")


@admin.register(Sale)
class SaleAdmin(ImportExportModelAdmin):
    """Административная панель для модели Sale."""
    resource_class = SaleResource

    list_display = ('store', 'sku', 'date', 'sales_type', 'sales_units',
                    'sales_units_promo', 'sales_rub', 'sales_run_promo')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    """Административная панель для модели Forecast."""

    list_display = ("store", "sku", "forecast_date")
