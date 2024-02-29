from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import UserProfile, Service
from .serializers import UserSerializer, UserProfileSerializer, ServiceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
