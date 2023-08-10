from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from users.models import Users
from users.api.serializers import UsersSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from users.api.pagination import CustomPagination


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('id', 'age')
    search_fields = ('id', 'last_name')
    ordering_fields = ('-id')
    pagination_class = CustomPagination
