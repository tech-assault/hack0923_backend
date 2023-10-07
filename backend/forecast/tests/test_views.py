import os
import sys

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from sale.models import Category

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, "api")
sys.path.append(CODE_DIR_PATH)


class CategoryAPITestCase(TestCase):
    """Тестирование CategoryViewSet."""

    def setUp(self):
        """Метод для настройки объектов."""
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
        """Тест получения списка категорий."""
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_category_detail(self):
        """Тест получения деталей категории."""
        category = Category.objects.get(sku="TestSKU")
        response = self.client.get(f"/api/categories/{category.sku}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["sku"], "TestSKU")

    def test_filter_categories_by_group(self):
        """Тест фильтрации категорий по группе."""
        response = self.client.get(
            "http://127.0.0.1:8000/api/categories/?group=TestCategoryGroup"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_categories_by_uom(self):
        """Тест фильтрации категорий по uom."""
        response = self.client.get("http://127.0.0.1:8000/api/categories/?uom=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
