from django.urls import path
from purchase import views

urlpatterns = [
    path('', views.all_purchase)
]
