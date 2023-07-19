from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from purchase.models import Purchases


def all_purchase(request):
    purchases = Purchases.objects.all()
    data = [{'id': purchases.id, 'date': purchases.date, 'user_id': purchases.user_id,
             'book_id': purchases.book_id}for purchases in purchases]
    return JsonResponse(data, safe=False)
