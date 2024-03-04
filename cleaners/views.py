from functools import reduce

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics, serializers
from .models import Cleaner, CleanerComment
from .serializers import CleanerSerializer, CleanerCommentSerializer
import operator
from django.db.models import Q

class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer

class CleanerSearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer

    def get_queryset(self):
        text = self.request.query_params.get('query', None)
        if not text:
            return self.request

        text_seq = text.split(' ')
        text_qs = reduce(operator.and_,
                         (Q(cv__icontains=x) for x in text_seq))

        return self.queryset.filter(text_qs)
class CleanerCommentListCreateView(generics.ListCreateAPIView):
    queryset = CleanerComment.objects.all()
    serializer_class = CleanerCommentSerializer

    def get_queryset(self):
        cleaner_id = self.kwargs.get('cleaner_id')
        return CleanerComment.objects.filter(cleaner_id=cleaner_id)
    def perform_create(self, serializer):
        cleaner_id = self.kwargs.get('cleaner_id')
        cleaner = get_object_or_404(Cleaner, id=cleaner_id)
        if CleanerComment.objects.filter(cleaner=cleaner, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this cleaner'})
        serializer.save(cleaner=self.request.user)
