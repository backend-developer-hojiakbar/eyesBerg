from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CleanerViewSet

router = DefaultRouter()
router.register(r'cleaners', CleanerViewSet)

urlpatterns = router.urls
