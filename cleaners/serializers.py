from rest_framework import serializers
from .models import Cleaner, CleanerComment

class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'
class CleanerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = "__all__"

