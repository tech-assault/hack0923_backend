from rest_framework import routers

from .views import CategoryViewSet, ForecastViewSet, SaleViewSet, StoreViewSet

router = routers.DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"stores", StoreViewSet, basename="stores")
router.register(r"sales", SaleViewSet, basename="sales")
router.register(r"forecast", ForecastViewSet, basename="forecast")

urlpatterns = router.urls
