from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy

from purchase.models import Purchases
from django.views.generic import ListView, DetailView, CreateView


class PurchaseListView(ListView):
    model = Purchases


class PurchaseDetailView(DetailView):
    model = Purchases


class PurchaseCreateView(CreateView):
    model = Purchases
    template_name = 'purchase/purchases_create.html'
    context_object_name = 'purchase/purchases_create.html'
    fields = ('user', 'book')
    success_url = reverse_lazy('purchases:purchases-list')
