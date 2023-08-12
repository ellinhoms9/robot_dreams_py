from rest_framework.viewsets import ModelViewSet
from book.models import Books
from book.api.serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookModelViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('id', 'price')
    search_fields = ('id', 'title')
    ordering_fields = ('-id')
