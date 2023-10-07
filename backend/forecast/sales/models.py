from django.db import models
from forecast.settings import MAX_LENGTH_FOR_FIELDS

from users.models import User


class Category(models.Model):
    """Модель категорий товаров."""

    sku = models.CharField(
        "Захэшированное id товара", primary_key=True, max_length=MAX_LENGTH_FOR_FIELDS
    )
    group = models.CharField(
        "Захэшированная группа товара", max_length=MAX_LENGTH_FOR_FIELDS
    )
    category = models.CharField(
        "Захэшированная категория товара", max_length=MAX_LENGTH_FOR_FIELDS
    )
    subcategory = models.CharField(
        "Захэшированная подкатегория товара", max_length=MAX_LENGTH_FOR_FIELDS
    )
    uom = models.PositiveSmallIntegerField(
        "Маркер, обозначающий продаётся товар на вес или в ШТ"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Store(models.Model):
    """Модель магазинов."""

    store = models.CharField(
        "Захэшированное id магазина", primary_key=True, max_length=MAX_LENGTH_FOR_FIELDS
    )
    users = models.ManyToManyField(User, related_name='stores')
    city = models.CharField(
        "Захэшированное id города", max_length=MAX_LENGTH_FOR_FIELDS
    )
    division = models.CharField(
        "Захэшированное id дивизиона", max_length=MAX_LENGTH_FOR_FIELDS
    )
    type_format = models.PositiveSmallIntegerField("id формата магазина")
    loc = models.PositiveSmallIntegerField("id тип локации / окружения магазина")
    size = models.PositiveSmallIntegerField("id типа размера магазина")
    is_active = models.BooleanField(
        "Флаг активного магазина на данный момент",
    )

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        permissions = [
            ("can_access_store", "Can access store"),
        ]


class Sale(models.Model):
    """Модель продаж."""

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, verbose_name="Захэшированное id магазина"
    )    
    sku = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Захэшированное id товара"
    )
    date = models.DateField("Дата")
    sales_type = models.BooleanField("Флаг наличия промо")
    sales_units = models.PositiveIntegerField(
        "Число проданных товаров без признака промо"
    )
    sales_units_promo = models.PositiveIntegerField(
        "Число проданных товаров с признаком промо"
    )
    sales_rub = models.FloatField("Продажи без признака промо в РУБ")
    sales_run_promo = models.FloatField("Продажи с признаком промо в РУБ")

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"


class Forecast(models.Model):
    """Модель прогнозов продаж."""

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, verbose_name="Захэшированное id магазина"
    )
    sku = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Захэшированное id товара"
    )
    forecast_date = models.DateField("Дата")
    sales_units_forecasted = models.PositiveIntegerField("Спрос в ШТ")
    

    class Meta:
        verbose_name = "Прогноз"
        verbose_name_plural = "Прогнозы"
