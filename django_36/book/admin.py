from django.contrib import admin
from book.models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price')
    search_fields = ('title', 'author')
