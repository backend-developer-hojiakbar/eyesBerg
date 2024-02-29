from django.shortcuts import render
from rest_framework import viewsets
from .models import Cleaner
from .serializers import CleanerSerializer

class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer
