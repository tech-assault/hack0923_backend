from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from forecast.settings import MAX_LENGTH_FOR_FIELDS

DECIMAL_VALIDATION = [MinValueValidator(Decimal('0.1'))]
MAX_DIGITS = 15
DECIMAL_PLACES = 1


class Category(models.Model):
    """Модель категорий товаров."""

    sku = models.CharField("Единица складского учета", primary_key=True,
                           max_length=MAX_LENGTH_FOR_FIELDS)
    group = models.CharField("Группа", max_length=MAX_LENGTH_FOR_FIELDS)
    category = models.CharField("Категория", max_length=MAX_LENGTH_FOR_FIELDS)
    subcategory = models.CharField("Подкатегория",
                                   max_length=MAX_LENGTH_FOR_FIELDS)
    uom = models.PositiveSmallIntegerField(
        "Маркер, обозначающий продаётся товар на вес или в ШТ")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.sku



class Store(models.Model):
    """Модель магазинов."""

    store = models.CharField("Название", primary_key=True,
                             max_length=MAX_LENGTH_FOR_FIELDS)
    city = models.CharField("Город", max_length=MAX_LENGTH_FOR_FIELDS)
    division = models.CharField("Дивизион", max_length=MAX_LENGTH_FOR_FIELDS)
    type_format = models.PositiveSmallIntegerField("Формат")
    loc = models.PositiveSmallIntegerField("Тип локации")
    size = models.PositiveSmallIntegerField("Тип размера")
    is_active = models.BooleanField("Флаг активного магазина на данный момент")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.store


class Sale(models.Model):
    """Модель продаж."""

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, verbose_name="Название магазина"
    )
    sku = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Единица складского учета")
    date = models.DateField("Дата")
    sales_type = models.BooleanField("Флаг наличия промо")
    sales_units = models.DecimalField(
        "Число проданных товаров без признака промо", max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES, validators=DECIMAL_VALIDATION)
    sales_units_promo = models.DecimalField(
        "Число проданных товаров с признаком промо", max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES, validators=DECIMAL_VALIDATION)
    sales_rub = models.DecimalField(
        "Продажи без признака промо в РУБ", max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES, validators=DECIMAL_VALIDATION)
    sales_run_promo = models.DecimalField(
        "Продажи с признаком промо в РУБ", max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES, validators=DECIMAL_VALIDATION)

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return f'{self.store} {self.sku} {self.date}'


class Forecast(models.Model):
    """Модель прогнозов продаж."""

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, verbose_name="Название магазина"
    )
    sku = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Единица складского учета"
    )
    forecast_date = models.DateField("Дата")
    sales_units_forecasted = models.PositiveIntegerField("Спрос в ШТ")

    class Meta:
        verbose_name = "Прогноз"
        verbose_name_plural = "Прогнозы"
