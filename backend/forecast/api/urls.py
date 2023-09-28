from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import CategoryViewSet, ForecastViewSet, SaleViewSet, StoreViewSet

router_v1 = routers.DefaultRouter()

router_v1.register(r"categories", CategoryViewSet, basename="categories")
router_v1.register(r"stores", StoreViewSet, basename="stores")
router_v1.register(r"sales", SaleViewSet, basename="sales")
router_v1.register(r"forecast", ForecastViewSet, basename="forecast")

urlpatterns = [
    path('', include(router_v1.urls)),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(), name="swagger"),
    path('redoc/', SpectacularRedocView.as_view(), name="redoc"),
]
