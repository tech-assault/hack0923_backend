from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Category, DayForecast, Sale, Store, SaleOfSkuInStore
from .resources import CategoryResource, StoreResource, SaleResource, \
    ForecastResource


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


@admin.register(SaleOfSkuInStore)
class SaleAdmin(ImportExportModelAdmin):
    """Административная панель для модели Sale."""
    resource_class = SaleResource

    list_display = ('get_store', 'get_sku', 'date', 'sales_type',
                    'sales_units', 'sales_units_promo', 'sales_rub',
                    'sales_run_promo')

    def get_store(self, obj):
        return obj.sku_of_store.store_id

    def get_sku(self, obj):
        return obj.sku_of_store.sku_id

    get_store.short_description = 'Магазин'
    get_sku.short_description = 'Единица складского учета'


@admin.register(DayForecast)
class ForecastAdmin(ImportExportModelAdmin):
    """Административная панель для модели Forecast."""
    resource_class = ForecastResource

    list_display = (
        'get_store', 'get_sku', 'get_forecast_date', 'date', 'units')

    def get_store(self, obj):
        return obj.forecast_sku_of_store.store.store

    def get_sku(self, obj):
        return obj.forecast_sku_of_store.sku.sku

    def get_forecast_date(self, obj):
        return obj.forecast_sku_of_store.forecast_date

    get_store.short_description = 'Магазин'
    get_sku.short_description = 'Единица складского учета'
    get_forecast_date.short_description = 'Дата расчета прогноза'

