from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from users.models import Users


def users_all(request):
    users = Users.objects.all()
    data = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
             'age': user.age} for user in users]
    return JsonResponse(data, safe=False)
