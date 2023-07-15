from django.http import HttpResponse
from django.shortcuts import render


def hello_users(request):
    return HttpResponse('Hello users!')
