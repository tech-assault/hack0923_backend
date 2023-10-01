from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export_celery.admin_actions import create_export_job_action
from import_export_celery.admin import ImportJobAdmin

from .models import Category, Forecast, Sale, Store
from .resource import CategoryResource, StoreResource, SaleResource


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

    list_display = ("store", "sku", "date", "sales_type", "sales_units",
                    "sales_units_promo", "sales_rub", "sales_run_promo",)


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    """Административная панель для модели Forecast."""

    actions = (
        create_export_job_action,
    )

    list_display = ("store", "forecast_date", "sku", "sales_units_forecasted")
