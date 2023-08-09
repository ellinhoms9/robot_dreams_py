from rest_framework import serializers
from purchase.models import Purchases


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ('user', 'book', 'date')
