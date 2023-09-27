from django.db import models


# Create your models here.
class Product(models.Model):
    sku = models.CharField('Единица складского учета', unique=True,
                           primary_key=True)
    group = models.CharField('Группа')
    category = models.CharField('Категория')
    subcategory = models.CharField('Подкатегория')
    uom = models.PositiveSmallIntegerField('Единица измерения')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Store(models.Model):
    store = models.CharField('Название', unique=True, primary_key=True)
    city = models.CharField('Город')
    division = models.CharField('Дивизион')
    type_format = models.PositiveSmallIntegerField('Формат')
    loc = models.PositiveSmallIntegerField('Локация')
    size = models.PositiveSmallIntegerField('Размер')
    is_active = models.BooleanField('Работает')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,
                              related_name='forecasts',
                              verbose_name='Магазин')
    sku = models.ForeignKey(Product, on_delete=models.CASCADE,
                            related_name='forecasts',
                            verbose_name='Товар')
    date = models.DateField('Дата')
    is_promo = models.BooleanField('Промо')
    sale_with_promo_in_units = models.PositiveIntegerField(
        'Число проданных товаров с признаком промо')
    sale_without_promo_in_units = models.PositiveIntegerField(
        'Число проданных товаров без признака промо;'
    )
    sale_with_promo_in_rub = models.DecimalField


class Forecast(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,
                              related_name='forecasts',
                              verbose_name='Магазин')
    sku = models.ForeignKey(Product, on_delete=models.CASCADE,
                            related_name='forecasts',
                            verbose_name='Товар')
    date = models.DateField('Дата')
    target = models.PositiveIntegerField('Количество')

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'
