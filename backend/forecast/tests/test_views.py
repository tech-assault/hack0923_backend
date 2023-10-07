import os
import sys
import unittest  # noqa
from datetime import date

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from sale.models import Category, Sale, Store

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, "api")
sys.path.append(CODE_DIR_PATH)


class CategoryAPITestCase(TestCase):
    """Тестирование CategoryViewSet."""

    def setUp(self):
        """Создание клиента API и тестовых данных категорий."""
        self.client = APIClient()
        self.category_data = {
            "sku": "TestSKU",
            "group": "TestCategoryGroup",
            "category": "TestCategory",
            "subcategory": "TestSubcategory",
            "uom": 1,
        }
        Category.objects.create(**self.category_data)

    def test_get_category_list(self):
        """
        Act: Получение списка категорий.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_category_detail(self):
        """
        Act: Получение детальной информации о категории.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка совпадения значения 'sku' в полученных данных с ожидаемым.
        """
        category = Category.objects.get(sku="TestSKU")
        response = self.client.get(f"/api/categories/{category.sku}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["sku"], "TestSKU")

    def test_filter_categories_by_group(self):
        """
        Act: Фильтрация категорий по полю 'group'.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get(
            "http://127.0.0.1:8000/api/categories/?group=TestCategoryGroup"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_categories_by_uom(self):
        """
        Act: Фильтрация категорий по полю 'uom'.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("http://127.0.0.1:8000/api/categories/?uom=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class StoreAPITestCase(TestCase):
    """Тестирование StoreViewSet."""

    def setUp(self):
        """Создание клиента API и тестовых данных магазина."""
        self.client = APIClient()
        self.store_data = {
            "store": "TestStore",
            "city": "TestCity",
            "division": "TestDivision",
            "type_format": 1,
            "loc": 1,
            "size": 1,
            "is_active": True,
        }
        self.store = Store.objects.create(**self.store_data)

    def test_get_store_list(self):
        """
        Act: Получение списка магазинов.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/shops/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_store_detail(self):
        """
        Act: Получение детальной информации о магазине.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get(f"/api/shops/{self.store.store}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["store"], "TestStore")

    def test_filter_stores_by_type_format(self):
        """
        Act: Фильтрация магазинов по типу формата.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/shops/?type_format=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_filter_stores_by_loc(self):
        """
        Act: Фильтрация магазинов по местоположению.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/shops/?loc=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_filter_stores_by_city(self):
        """
        Act: Фильтрация магазинов по городу.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/shops/?city=TestCity")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_filter_stores_by_division(self):
        """
        Act: Фильтрация магазинов по подразделению.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 1).
        """
        response = self.client.get("/api/shops/?division=TestDivision")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_invalid_type_format_value(self):
        """
        Act: Попытка фильтрации магазинов по неправильному значению типа формата.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 0).
        """
        response = self.client.get("/api/shops/?type_format=999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_invalid_loc_value(self):
        """
        Act: Попытка фильтрации магазинов по неправильному значению местоположения.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 0).
        """
        response = self.client.get("/api/shops/?loc=999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_invalid_city_value(self):
        """
        Act: Попытка фильтрации магазинов по неправильному значению города.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 0).
        """
        response = self.client.get("/api/shops/?city=Nonexist")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_invalid_division_value(self):
        """
        Act: Попытка фильтрации магазинов по неправильному значению подразделения.

        Assert:
        - Проверка статуса ответа (HTTP 200 OK).
        - Проверка количества полученных данных (должно быть 0).
        """
        response = self.client.get("/api/shops/?division=Nonexist")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


class SaleViewSetTestCase(TestCase):
    """Тестирование SaleViewSet."""

    def setUp(self):
        """Создание клиента API и тестовых данных магазинов, категорий и продаж."""
        self.client = APIClient()
        self.store = Store.objects.create(store="TestStore")
        self.category = Category.objects.create(sku="TestSKU")
        self.sale_data = {
            "store": self.store,
            "sku": self.category,
            "date": date.today(),
            "sales_type": True,
            "sales_units": 10,
            "sales_units_promo": 5,
            "sales_rub": 100.0,
            "sales_run_promo": 50.0,
        }
        Sale.objects.create(**self.sale_data)

    def test_list_sales(self):
        """
        Act: Получение списка продаж для магазина.

        Assert: Проверка статуса ответа, количества полученных данных.
        """
        response = self.client.get("/api/sales/", {"store": self.store.store})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["store"], "TestStore")

    def test_retrieve_sale(self):
        """
        Act: Получение деталей продажи для магазина и категории.

        Assert: Проверка статуса ответа и соответствия полученных данных ожидаемым.
        """
        response = self.client.get(
            f"/api/sales/{self.category.sku}/",
            {"store": self.store.store, "sku": self.category.sku},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["store"], "TestStore")
        self.assertEqual(response.data["sku"], "TestSKU")

    def test_invalid_list_sales(self):
        """
        Act: Получение списка продаж для неверного магазина.

        Assert: Проверка статуса ответа и отсутствия данных.
        """
        response = self.client.get("/api/sales/", {"store": "InvalidStore"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_invalid_retrieve_sale(self):
        """
        Act: Получение деталей продажи для неверного магазина и категории.

        Assert: Проверка статуса ответа и соответствия полученных данных ожидаемым.
        """
        response = self.client.get(
            "/api/sales/InvalidSKU/",
            {"store": "InvalidStore", "sku": "InvalidSKU"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"store": "InvalidStore", "sku": "InvalidSKU", "fact": []}
        )
