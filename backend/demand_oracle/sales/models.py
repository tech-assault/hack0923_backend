from django.db import models


class Category(models.Model):
    """Модель для категорий товаров."""

    sku = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200)
    uom = models.IntegerField()


class Store(models.Model):
    """Модель для магазинов."""

    store = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    type_format = models.IntegerField()
    loc = models.IntegerField()
    size = models.IntegerField()
    is_active = models.BooleanField()


class Sale(models.Model):
    """Модель для продаж."""

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sku = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    sales_type = models.IntegerField()
    sales_units = models.IntegerField()
    sales_units_promo = models.IntegerField()
    sales_rub = models.FloatField()
    sales_run_promo = models.FloatField()


class Forecast(models.Model):
    """Модель для прогнозов продаж."""

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    forecast_date = models.DateField()
    sku = models.ForeignKey(Category, on_delete=models.CASCADE)
    sales_units_forecasted = models.IntegerField()
