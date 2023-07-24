from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from purchase.models import Purchases
from book.models import Books
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from users.models import Users


@admin.register(get_user_model())
class UsersAdmin(UserAdmin):
    pass


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price')
    search_fields = ('title', 'author')


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'date')
    search_fields = ('user__first_name', 'user__last_name', 'book__title')
