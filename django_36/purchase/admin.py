from django.contrib import admin
from purchase.models import Purchases


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'date')
    search_fields = ('user__first_name', 'user__last_name', 'book__title')
