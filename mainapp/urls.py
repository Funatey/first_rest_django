from rest_framework.routers import DefaultRouter
from .views import CarsViewSet
router = DefaultRouter()
router.register('cars', CarsViewSet)

urlpatterns = router.urls
