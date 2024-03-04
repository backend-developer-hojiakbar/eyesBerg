from rest_framework import serializers
from .models import Cleaner, CleanerComment
from django.urls import reverse
class CleanerCommentSerializer(serializers.ModelSerializer):
    cleaner = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = CleanerComment
        fields = "__all__"

class CleanerSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Cleaner
        fields = '__all__'

    def get_comments(self, obj):
        comments = CleanerComment.objects.filter(cleaner=obj)[:3]
        request = self.context.get('request')
        return {
            'comments': CleanerCommentSerializer(comments, many=True).data,
            'all_comment_link': request.build_absolute_uri(reverse('cleaner-comments', kwargs={'cleaner_id': obj.id}))
        }


