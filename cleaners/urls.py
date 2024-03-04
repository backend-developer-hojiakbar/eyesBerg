from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CleanerViewSet, CleanerSearchViewSet

router = DefaultRouter()
router.register(r'cleaners', CleanerViewSet)
router.register('search',
                CleanerSearchViewSet,
                basename='search-cleaner')

urlpatterns = router.urls

