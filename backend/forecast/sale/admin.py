from django.contrib import admin

from .models import Category, Forecast, Sale, Store


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административная панель для модели Category."""

    list_display = ('pr_sku_id', 'pr_group_id', 'pr_cat_id', 'pr_subcat_id',
                    'pr_uom_id')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Административная панель для модели Store."""

    list_display = (
        'st_id', 'st_city_id', 'st_division_code', 'st_type_format_id',
        'st_type_loc_id', 'st_type_size_id', 'st_is_active')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """Административная панель для модели Sale."""

    list_display = (
        'st_id', 'pr_sku_id', 'date', 'pr_sales_type_id', 'pr_sales_in_units',
        'pr_promo_sales_in_units', 'pr_sales_in_rub', 'pr_promo_sales_in_rub')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    """Административная панель для модели Forecast."""

    list_display = ('st_id', 'pr_sku_id', 'date', 'target')
