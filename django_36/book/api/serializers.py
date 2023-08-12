from rest_framework import serializers
from book.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'author', 'year', 'price')
