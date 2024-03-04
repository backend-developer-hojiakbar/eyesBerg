from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'login', obtain_auth_token)
urlpatterns = [
    path('', include(router.urls)),
]