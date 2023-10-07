from decimal import Decimal

from django.test import TestCase
from sale.models import Category, DayForecast, Forecast, Sale, Store


class CategoryModelTestCase(TestCase):
    """Тесты для модели Category."""

    def setUp(self):
        """Настройка данных для тестирования."""
        self.category = Category.objects.create(
            sku="SKU001",
            group="Group1",
            category="Category1",
            subcategory="Subcategory1",
            uom=1,
        )

    def test_category_str(self):
        """Проверка строкового представления Category."""
        self.assertEqual(str(self.category), "SKU001")

    def test_category_fields(self):
        """Проверка значений полей Category."""
        self.assertEqual(self.category.group, "Group1")
        self.assertEqual(self.category.category, "Category1")
        self.assertEqual(self.category.subcategory, "Subcategory1")
        self.assertEqual(self.category.uom, 1)

    def test_category_verbose_names(self):
        """Проверка текстовых меток (verbose_name) полей Category."""
        self.assertEqual(
            self.category._meta.get_field("sku").verbose_name,
            "Единица складского учета",
        )
        self.assertEqual(self.category._meta.get_field("group").verbose_name, "Группа")
        self.assertEqual(
            self.category._meta.get_field("category").verbose_name, "Категория"
        )
        self.assertEqual(
            self.category._meta.get_field("subcategory").verbose_name, "Подкатегория"
        )
        self.assertEqual(
            self.category._meta.get_field("uom").verbose_name,
            "Маркер, обозначающий продаётся товар на вес или в ШТ",
        )
        self.assertEqual(self.category._meta.verbose_name, "Категория")
        self.assertEqual(self.category._meta.verbose_name_plural, "Категории")

    def test_category_max_length(self):
        """Проверка максимальной длины полей Category."""
        self.assertLessEqual(
            len(self.category.sku), Category._meta.get_field("sku").max_length
        )
        self.assertLessEqual(
            len(self.category.group), Category._meta.get_field("group").max_length
        )
        self.assertLessEqual(
            len(self.category.category), Category._meta.get_field("category").max_length
        )
        self.assertLessEqual(
            len(self.category.subcategory),
            Category._meta.get_field("subcategory").max_length,
        )


class StoreModelTestCase(TestCase):
    """Тесты для модели Store."""

    def setUp(self):
        """Настройка данных для тестирования."""
        self.store = Store.objects.create(
            store="Store1",
            city="City1",
            division="Division1",
            type_format=1,
            loc=1,
            size=1,
            is_active=True,
        )

    def test_store_str(self):
        """Проверка строкового представления Store."""
        self.assertEqual(str(self.store), "Store1")

    def test_store_fields(self):
        """Проверка значений полей Store."""
        self.assertEqual(self.store.city, "City1")
        self.assertEqual(self.store.division, "Division1")
        self.assertEqual(self.store.type_format, 1)
        self.assertEqual(self.store.loc, 1)
        self.assertEqual(self.store.size, 1)
        self.assertEqual(self.store.is_active, True)

    def test_store_verbose_names(self):
        """Проверка текстовых меток (verbose_name) полей Store."""
        self.assertEqual(self.store._meta.get_field("store").verbose_name, "Название")
        self.assertEqual(self.store._meta.get_field("city").verbose_name, "Город")
        self.assertEqual(
            self.store._meta.get_field("division").verbose_name, "Дивизион"
        )
        self.assertEqual(
            self.store._meta.get_field("type_format").verbose_name, "Формат"
        )
        self.assertEqual(self.store._meta.get_field("loc").verbose_name, "Тип локации")
        self.assertEqual(self.store._meta.get_field("size").verbose_name, "Тип размера")
        self.assertEqual(
            self.store._meta.get_field("is_active").verbose_name,
            "Флаг активного магазина на данный момент",
        )
        self.assertEqual(self.store._meta.verbose_name, "Магазин")
        self.assertEqual(self.store._meta.verbose_name_plural, "Магазины")

    def test_store_max_length(self):
        """Проверка максимальной длины полей Store."""
        self.assertLessEqual(
            len(self.store.store), Store._meta.get_field("store").max_length
        )
        self.assertLessEqual(
            len(self.store.city), Store._meta.get_field("city").max_length
        )
        self.assertLessEqual(
            len(self.store.division), Store._meta.get_field("division").max_length
        )


class SaleModelTestCase(TestCase):
    """Тесты для модели Sale."""

    def setUp(self):
        """Настройка данных для тестирования."""
        self.store = Store.objects.create(
            store="Store1",
            city="City1",
            division="Division1",
            type_format=1,
            loc=1,
            size=1,
            is_active=True,
        )
        self.category = Category.objects.create(
            sku="SKU001",
            group="Group1",
            category="Category1",
            subcategory="Subcategory1",
            uom=1,
        )
        self.sale = Sale.objects.create(
            store=self.store,
            sku=self.category,
            date="2023-10-01",
            sales_type=True,
            sales_units=Decimal("100.5"),
            sales_units_promo=Decimal("50.5"),
            sales_rub=Decimal("1000.5"),
            sales_run_promo=Decimal("500.5"),
        )

    def test_sale_str(self):
        """Проверка строкового представления Sale."""
        expected_str = "Store1 SKU001"
        self.assertEqual(str(self.sale), expected_str)

    def test_sale_fields(self):
        """Проверка значений полей Sale."""
        self.assertEqual(self.sale.store, self.store)
        self.assertEqual(self.sale.sku, self.category)
        self.assertEqual(str(self.sale.date), "2023-10-01")
        self.assertEqual(self.sale.sales_type, True)
        self.assertEqual(self.sale.sales_units, Decimal("100.5"))
        self.assertEqual(self.sale.sales_units_promo, Decimal("50.5"))
        self.assertEqual(self.sale.sales_rub, Decimal("1000.5"))
        self.assertEqual(self.sale.sales_run_promo, Decimal("500.5"))

    def test_sale_verbose_names(self):
        """Проверка текстовых меток (verbose_name) полей Sale."""
        self.assertEqual(
            self.sale._meta.get_field("store").verbose_name, "Название магазина"
        )
        self.assertEqual(
            self.sale._meta.get_field("sku").verbose_name, "Единица складского учета"
        )
        self.assertEqual(self.sale._meta.get_field("date").verbose_name, "Дата")
        self.assertEqual(
            self.sale._meta.get_field("sales_type").verbose_name, "Флаг наличия промо"
        )
        self.assertEqual(
            self.sale._meta.get_field("sales_units").verbose_name,
            "Число проданных товаров без признака промо",
        )
        self.assertEqual(
            self.sale._meta.get_field("sales_units_promo").verbose_name,
            "Число проданных товаров с признаком промо",
        )
        self.assertEqual(
            self.sale._meta.get_field("sales_rub").verbose_name,
            "Продажи без признака промо в РУБ",
        )
        self.assertEqual(
            self.sale._meta.get_field("sales_run_promo").verbose_name,
            "Продажи с признаком промо в РУБ",
        )
        self.assertEqual(self.sale._meta.verbose_name, "Продажа")
        self.assertEqual(self.sale._meta.verbose_name_plural, "Продажи")


class ForecastModelTestCase(TestCase):
    """Тесты для модели Forecast."""

    def setUp(self):
        """Настройка данных для тестирования."""
        self.store = Store.objects.create(
            store="Store1",
            city="City1",
            division="Division1",
            type_format=1,
            loc=1,
            size=1,
            is_active=True,
        )
        self.category = Category.objects.create(
            sku="SKU001",
            group="Group1",
            category="Category1",
            subcategory="Subcategory1",
            uom=1,
        )
        self.forecast = Forecast.objects.create(
            store=self.store,
            sku=self.category,
            forecast_date="2023-10-01",
        )

    def test_str_representation(self):
        """Проверка строкового представления модели."""
        expected_str = (
            f"{self.store.store} {self.category.sku} {self.forecast.forecast_date}"
        )
        self.assertEqual(str(self.forecast), expected_str)

    def test_verbose_name(self):
        """Проверка значений полей verbose_name."""
        self.assertEqual(
            self.forecast._meta.get_field("store").verbose_name, "Название магазина"
        )
        self.assertEqual(
            self.forecast._meta.get_field("sku").verbose_name,
            "Единица складского учета",
        )
        self.assertEqual(
            self.forecast._meta.get_field("forecast_date").verbose_name,
            "Дата расчета прогноза",
        )


class DayForecastModelTestCase(TestCase):
    """Тесты для модели DayForecast."""

    def setUp(self):
        """Настройка данных для тестирования."""
        self.store = Store.objects.create(
            store="Store1",
            city="City1",
            division="Division1",
            type_format=1,
            loc=1,
            size=1,
            is_active=True,
        )
        self.category = Category.objects.create(
            sku="SKU001",
            group="Group1",
            category="Category1",
            subcategory="Subcategory1",
            uom=1,
        )
        self.forecast = Forecast.objects.create(
            store=self.store,
            sku=self.category,
            forecast_date="2023-10-01",
        )
        self.day_forecast = DayForecast.objects.create(
            forecast_sku_of_store=self.forecast,
            date="2023-10-02",
            units=50,
        )

    def test_verbose_name(self):
        """Проверка значений полей verbose_name."""
        self.assertEqual(
            self.day_forecast._meta.get_field("forecast_sku_of_store").verbose_name,
            "Дата прогноза",
        )
        self.assertEqual(self.day_forecast._meta.get_field("date").verbose_name, "Дата")
        self.assertEqual(
            self.day_forecast._meta.get_field("units").verbose_name, "Спрос в ШТ"
        )
