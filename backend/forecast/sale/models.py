from django.db import models

from forecast.settings import MAX_LENGTH_FOR_FIELDS


class Category(models.Model):
    """Модель категорий товаров."""
    pr_sku_id = models.CharField('Захэшированное id товара', primary_key=True,
                                 max_length=MAX_LENGTH_FOR_FIELDS)
    pr_group_id = models.CharField('Захэшированная группа товара',
                                   max_length=MAX_LENGTH_FOR_FIELDS)
    pr_cat_id = models.CharField('Захэшированная категория товара',
                                 max_length=MAX_LENGTH_FOR_FIELDS)
    pr_subcat_id = models.CharField('Захэшированная подкатегория товара',
                                    max_length=MAX_LENGTH_FOR_FIELDS)
    pr_uom_id = models.PositiveSmallIntegerField(
        'Маркер, обозначающий продаётся товар на вес или в ШТ')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Store(models.Model):
    """Модель магазинов."""

    st_id = models.CharField('Захэшированное id магазина', primary_key=True,
                             max_length=MAX_LENGTH_FOR_FIELDS)
    st_city_id = models.CharField('Захэшированное id города',
                                  max_length=MAX_LENGTH_FOR_FIELDS)
    st_division_code = models.CharField('Захэшированное id дивизиона',
                                        max_length=MAX_LENGTH_FOR_FIELDS)
    st_type_format_id = models.PositiveSmallIntegerField(
        'id формата магазина', max_length=MAX_LENGTH_FOR_FIELDS)
    st_type_loc_id = models.PositiveSmallIntegerField(
        'id тип локации / окружения магазина',
        max_length=MAX_LENGTH_FOR_FIELDS)
    st_type_size_id = models.PositiveSmallIntegerField(
        'id типа размера магазина', max_length=MAX_LENGTH_FOR_FIELDS)
    st_is_active = models.BooleanField(
        'флаг активного магазина на данный момент', )

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Sale(models.Model):
    """Модель продаж."""

    st_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                              verbose_name='Захэшированное id магазина')
    pr_sku_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                  verbose_name='Захэшированное id товара')
    date = models.DateField('Дата')
    pr_sales_type_id = models.BooleanField('Флаг наличия промо')
    pr_sales_in_units = models.PositiveIntegerField(
        'Число проданных товаров без признака промо')
    pr_promo_sales_in_units = models.PositiveIntegerField(
        'Число проданных товаров с признаком промо')
    pr_sales_in_rub = models.FloatField('продажи без признака промо в РУБ')
    pr_promo_sales_in_rub = models.FloatField(
        'продажи с признаком промо в РУБ')

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'


class Forecast(models.Model):
    """Модель прогнозов продаж."""

    st_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                              verbose_name='Захэшированное id магазина')
    pr_sku_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                  verbose_name='Захэшированное id товара')
    date = models.DateField('Дата')
    target = models.PositiveIntegerField('спрос в ШТ')

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'
