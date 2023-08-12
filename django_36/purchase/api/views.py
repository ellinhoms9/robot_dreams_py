from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from purchase.models import Purchases
from purchase.api.serializers import PurchaseSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('book', 'user')
    search_fields = ('id', 'user')
    ordering_fields = ('-id')
