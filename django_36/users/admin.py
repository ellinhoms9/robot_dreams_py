from purchase.models import Purchases
from book.models import Books
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price')
    search_fields = ('title', 'author')


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'date')
    search_fields = ('user__first_name', 'user__last_name', 'book__title')
